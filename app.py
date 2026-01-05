import streamlit as st
from langgraph_app import run_graph

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Smart Job Application Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Smart Job Application Assistant")

# ---------------- Inputs ----------------
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=200
)

job_role = st.text_input(
    "Job Role (e.g. Backend Developer)"
)

analyze = st.button("Analyze Job Application")

# ---------------- Action ----------------
if analyze:
    if resume_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    if not jd_text.strip():
        st.warning("Please paste a job description.")
        st.stop()

    if not job_role.strip():
        st.warning("Please enter job role.")
        st.stop()

    # --------- DIRECT TEST (NO LANGGRAPH) ---------
    from agents.resume_parser import parse_resume
    from agents.jd_parser import parse_jd
    from agents.skill_matcher import match_skills
    from agents.fit_score import calculate_fit
    from agents.cover_letter import generate_cover_letter

    resume_text = parse_resume(resume_file)
    jd_clean = parse_jd(jd_text)

    matched, jd_skills = match_skills(resume_text, jd_clean)
    fit_score = calculate_fit(matched, jd_skills)

    cover_letter = generate_cover_letter(job_role, matched)

    st.success("Analysis Completed!")

    st.subheader("📊 Job Fit Score")
    st.progress(fit_score / 100)
    st.write(f"{fit_score}% Match")

    st.subheader("🧠 Matched Skills")
    st.write(matched)

    st.subheader("📝 AI Generated Cover Letter")
    st.write(cover_letter)
