def final_score(match_score, interest_score):
    return round((0.7 * match_score) + (0.3 * interest_score), 2)