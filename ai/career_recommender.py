def recommend_career(skills):
    if "react" in skills:
        return "Frontend Developer"
    elif "python" in skills:
        return "Backend Developer"
    elif "sql" in skills:
        return "Data Analyst"
    else:
        return "Software Developer"