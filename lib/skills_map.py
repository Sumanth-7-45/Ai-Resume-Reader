SKILL_MAP = {
    "python": ["python"],
    "flask": ["flask"],
    "rest api": ["rest api", "restful api", "restful apis"],
    "sql": ["sql", "mysql", "postgresql"],
    "git": ["git", "github"]
}

TIME_PATTERNS = [
    r"over\s*(\d+)\s*years?",
    r"more than\s*(\d+)\s*years?",
    r"for\s*(\d+)\s*years?",
    r"(\d+)\s*\+\s*years?",
    r"(\d+)\s*years?",
    r"(\d+)\s*months?"
]

ACTION_WORDS = [
    "worked", "working", "developed", "built",
    "designed", "implemented", "managed", "created"
]
