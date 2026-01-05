from langgraph.graph import StateGraph, END

from agents.resume_parser import parse_resume
from agents.jd_parser import parse_jd
from agents.skill_matcher import match_skills
from agents.fit_score import calculate_fit
from agents.cover_letter import generate_cover_letter


class State(dict):
    pass


def resume_agent(state):
    resume_file = state.get("resume_file")
    state["resume_text"] = parse_resume(resume_file) if resume_file else ""
    return state


def jd_agent(state):
    jd_raw = state.get("jd_text_raw", "")
    state["jd_text"] = parse_jd(jd_raw) if jd_raw else ""
    return state


def skill_agent(state):
    matched, jd_skills = match_skills(
        state.get("resume_text", ""),
        state.get("jd_text", "")
    )
    state["matched"] = matched
    state["jd_skills"] = jd_skills
    return state


def score_agent(state):
    state["fit_score"] = calculate_fit(
        state.get("matched", []),
        state.get("jd_skills", [])
    )
    return state


def cover_agent(state):
    role = state.get("job_role", "")
    matched = state.get("matched", [])
    state["cover_letter"] = (
        generate_cover_letter(role, matched)
        if role and matched
        else "Not enough data to generate cover letter."
    )
    return state


graph = StateGraph(State)

graph.add_node("resume", resume_agent)
graph.add_node("jd", jd_agent)
graph.add_node("skills", skill_agent)
graph.add_node("score", score_agent)
graph.add_node("cover", cover_agent)

graph.set_entry_point("resume")

graph.add_edge("resume", "jd")
graph.add_edge("jd", "skills")
graph.add_edge("skills", "score")
graph.add_edge("score", "cover")
graph.add_edge("cover", END)   # ✅ FINAL STATE

app = graph.compile()


def run_graph(input_state: dict):
    return app.invoke(input_state)
