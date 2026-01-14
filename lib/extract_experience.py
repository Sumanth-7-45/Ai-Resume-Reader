import re
from lib.skills_map import TIME_PATTERNS, ACTION_WORDS

def extract_sentence_experience(text):
    sentences = re.split(r"[.\n]", text)
    experiences = []

    for sentence in sentences:
        if any(word in sentence for word in ACTION_WORDS):
            for pattern in TIME_PATTERNS:
                match = re.search(pattern, sentence)
                if match:
                    value = int(match.group(1))

                    if "month" in pattern:
                        value = round(value / 12, 1)

                    experiences.append(value)
               

    return max(experiences) if experiences else 0
