from utils.constants import SKILLS

def match_skills(resume_text, jd_text):
    resume_skills = [s for s in SKILLS if s in resume_text]
    jd_skills = [s for s in SKILLS if s in jd_text]

    matched = list(set(resume_skills) & set(jd_skills))

    return matched, jd_skills
