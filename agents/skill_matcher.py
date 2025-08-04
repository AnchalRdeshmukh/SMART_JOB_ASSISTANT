def extract_keywords(text):
    return set(word.lower() for word in text.split() if len(word) > 3)

def match_skills(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)
    matched_skills = resume_keywords.intersection(jd_keywords)
    return list(matched_skills)
