skills_db = ["python", "java", "react", "sql", "html", "css"]

def match_skills(text):
    matched = [skill for skill in skills_db if skill in text]
    missing = [skill for skill in skills_db if skill not in matched]

    score = int((len(matched) / len(skills_db)) * 100)

    return {
        "skills_found": matched,
        "missing_skills": missing,
        "score": score
    }