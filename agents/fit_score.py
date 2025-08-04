from agents.skill_matcher import match_skills
from utils.constants import MATCH_THRESHOLD, FIT_SCORE_LABELS

def calculate_fit_score(resume_text, jd_text):
    matched_skills = match_skills(resume_text, jd_text)
    score = len(matched_skills)
    return score, matched_skills
def interpret_score(score):
    if score <= 0.4:
        return FIT_SCORE_LABELS["0-0.4"]
    elif score <= 0.7:
        return FIT_SCORE_LABELS["0.4-0.7"]
    else:
        return FIT_SCORE_LABELS["0.7-1.0"]
