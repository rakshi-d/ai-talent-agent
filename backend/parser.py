import re

def parse_jd(jd_text):
    skills = []
    
    if "python" in jd_text.lower():
        skills.append("Python")
    if "machine learning" in jd_text.lower():
        skills.append("Machine Learning")
    if "deep learning" in jd_text.lower():
        skills.append("Deep Learning")

    exp_match = re.search(r'(\d+)\+?\s*years', jd_text)
    experience = int(exp_match.group(1)) if exp_match else 0

    location = "Chennai" if "chennai" in jd_text.lower() else "Any"

    return {
        "skills": skills,
        "experience": experience,
        "location": location
    }