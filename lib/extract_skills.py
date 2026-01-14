from lib.skills_map import SKILL_MAP

def extract_skills(text):
    found = set()

    for skill, variants in SKILL_MAP.items():
        for v in variants:
            if v in text:
                found.add(skill)

    return list(found)
