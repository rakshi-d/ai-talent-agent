def calculate_match_score(candidate, jd):
    explanations = []

    # Skill match
    matched_skills = list(set(candidate["skills"]) & set(jd["skills"]))
    skill_matches = len(matched_skills)
    
    if jd["skills"]:
        skill_score = (skill_matches / len(jd["skills"])) * 50
    else:
        skill_score = 0

    explanations.append(f"Matched skills: {matched_skills}")

    # Experience
    if candidate["experience"] >= jd["experience"]:
        exp_score = 30
        explanations.append(f"Experience OK: {candidate['experience']} years")
    else:
        exp_score = 10
        explanations.append(f"Less experience: {candidate['experience']} years")

    # Location
    if candidate["location"] == jd["location"]:
        loc_score = 20
        explanations.append("Location match")
    else:
        loc_score = 5
        explanations.append("Different location")

    total = round(skill_score + exp_score + loc_score, 2)

    return total, explanations