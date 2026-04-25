def simulate_chat(candidate):
    if candidate["status"] == "actively looking":
        return {
            "interest_score": 90,
            "response": "Yes, I am actively looking for new opportunities."
        }
    elif candidate["status"] == "open":
        return {
            "interest_score": 70,
            "response": "I am open to hearing about this role."
        }
    else:
        return {
            "interest_score": 30,
            "response": "Not interested currently."
        }