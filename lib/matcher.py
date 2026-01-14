from lib.text_extract import extract_text_from_pdf
from lib.extract_skills import extract_skills
from lib.extract_experience import extract_sentence_experience

def match_resume(pdf_path, jd_skills, jd_experience):
    text = extract_text_from_pdf(pdf_path)

    skills = extract_skills(text)
    experience = extract_sentence_experience(text)

    matched = set(skills).intersection(set(jd_skills))
    skill_score = round(len(matched) / len(jd_skills) * 100, 2)

    return {
        "skills_found": skills,
        "matched_skills": list(matched),
        "skill_match_percent": skill_score,
        "experience_years": experience,
        "experience_required": jd_experience,
        "experience_match": experience >= jd_experience
    }
