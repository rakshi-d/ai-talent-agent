from flask import Flask, request, jsonify, render_template
import json
from collections import OrderedDict
from parser import parse_jd
from matcher import calculate_match_score
from chat import simulate_chat
from scorer import final_score
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Load candidates
with open("data.json") as f:
    candidates = json.load(f)

# ✅ HOME ROUTE (for browser)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ THIS IS /process ROUTE (ADD HERE)
@app.route("/process", methods=["POST"])
def process():
    jd_text = request.json.get("jd")
    jd = parse_jd(jd_text)

    results = []

    for c in candidates:
        match, explanation = calculate_match_score(c, jd)
        
        if match < 50:
            continue
        
        chat_data = simulate_chat(c)
        interest = chat_data["interest_score"]
        response = chat_data["response"]
        
        final = final_score(match, interest)

        results.append(OrderedDict([
            ("name", c["name"]),
            ("match_score", match),
            ("interest_score", interest),
            ("final_score", final),
            ("chat_response", response),
            ("explanation", explanation)
        ]))

    results.sort(key=lambda x: x["final_score"], reverse=True)

    return jsonify(results)

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)