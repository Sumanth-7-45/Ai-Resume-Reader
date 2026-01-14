from lib.matcher import match_resume
from flask import Flask, request, jsonify

if __name__ == "__main__":
    JOB_DESCRIPTION = {
        "skills": ["python", "flask", "rest api", "sql", "git"],
        "experience": 2
    }

    PDF_RESUME = r".venv/Sumanth S__U06PE23S0016.pdf"

    result = match_resume(PDF_RESUME,JOB_DESCRIPTION["skills"],JOB_DESCRIPTION["experience"])

    print("\n--- ATS SENTENCE EXPERIENCE RESULT ---")
    for key, value in result.items():
        print(f"{key}: {value}")
