# langgraph_app.py

from langgraph.graph import StateGraph, END
from agents.jd_parser import parse_job_description
from agents.resume_parser import parse_resume
from agents.skill_matcher import match_skills
from agents.fit_score import calculate_fit_score

# 1. Define a state structure
state = {
    "resume": None,
    "jd": None,
    "parsed_resume": None,
    "parsed_jd": None,
    "matched_skills": None,
    "fit_score": None,
}

# 2. Define each node as a function

def load_resume(state):
    with open("sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()
    state["resume"] = resume_text
    return state

def load_jd(state):
    with open("sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()
    state["jd"] = jd_text
    return state

def run_resume_parser(state):
    parsed = parse_resume(state["resume"])
    state["parsed_resume"] = parsed
    return state

def run_jd_parser(state):
    parsed = parse_job_description(state["jd"])
    state["parsed_jd"] = parsed
    return state

def run_skill_matcher(state):
    matched = match_skills(state["parsed_resume"], state["parsed_jd"])
    state["matched_skills"] = matched
    return state

def run_fit_score(state):
    score = calculate_fit_score(state["matched_skills"])
    state["fit_score"] = score
    return state

# 3. Build LangGraph
builder = StateGraph(state)

builder.add_node("load_resume", load_resume)
builder.add_node("load_jd", load_jd)
builder.add_node("parse_resume", run_resume_parser)
builder.add_node("parse_jd", run_jd_parser)
builder.add_node("match_skills", run_skill_matcher)
builder.add_node("fit_score", run_fit_score)

# Connect nodes step-by-step
builder.set_entry_point("load_resume")
builder.add_edge("load_resume", "load_jd")
builder.add_edge("load_jd", "parse_resume")
builder.add_edge("parse_resume", "parse_jd")
builder.add_edge("parse_jd", "match_skills")
builder.add_edge("match_skills", "fit_score")
builder.add_edge("fit_score", END)

# Compile the graph
graph = builder.compile()

# 4. Run the graph
final_output = graph.invoke({})

# 5. Print the final score
print("\n✅ Final Fit Score:")
print(final_output["fit_score"])
