#  AI-Powered Talent Scouting & Engagement Agent

##  Overview

Recruiters often spend a lot of time manually filtering candidates and checking their interest. This project aims to simplify that process by building an AI-based agent that can automatically match candidates to a job description and estimate their interest level.

The system takes a Job Description (JD) as input, finds relevant candidates, evaluates them based on skills and experience, simulates their interest, and provides a ranked shortlist.

---

Live Website URL: https://ai-talent-agent-kc4g.onrender.com/

## ⚙️ Features

- Parses job descriptions to extract key requirements
- Matches candidates based on skills, experience, and location
- Simulates candidate interest using a simple conversational logic
- Generates:
  - Match Score
  - Interest Score
  - Final Score (ranking)
- Filters out irrelevant candidates
- Displays results in a clean UI table
- Handles edge cases (e.g., no matching candidates)

---

## 🧠 How It Works

1. The recruiter enters a job description in the UI  
2. The frontend sends the request to the Flask backend  
3. The backend processes it through multiple modules:
   - **JD Parser** → extracts skills, experience, location  
   - **Matcher** → compares candidates with JD  
   - **Chat Simulator** → estimates candidate interest  
   - **Scoring Engine** → calculates final ranking  
4. Results are returned and displayed in a structured table  

---

##  Scoring Logic

- **Match Score**
  - Skills → 50%
  - Experience → 30%
  - Location → 20%

- **Interest Score**
  - Actively looking → High
  - Open → Medium
  - Not interested → Low

- **Final Score**
Final Score = 0.7 × Match Score + 0.3 × Interest Score



---

##  Architecture Diagram
(architecture.png)

### Architecture Explanation

This project follows a simple client-server architecture.

The user interacts with a frontend interface to enter a job description. This input is sent to the Flask backend via an API. The backend processes the request using multiple modules such as parsing, matching, interest simulation, and scoring.

Candidate data is stored in a JSON file, and the system evaluates each candidate before returning a ranked list to the frontend.

---

##  How to Run the Project Locally

### 1. Clone the repository
git clone https://github.com/rakshi-d/ai-talent-agent.git

### 2. Go to backend folder
cd ai-talent-agent/backend

### 3. Install dependencies
pip install flask flask-cors

### 4. Run the server
python app.py

You should see:
Running on http://127.0.0.1:5000

### 5. Open in browser
http://127.0.0.1:5000

---

##  Sample Input 1

Looking for a Python developer with 2+ years of experience in Machine Learning. Location: Chennai.

---

## Sample Output

- Ranked list of candidates
- Match Score
- Interest Score
- Final Score
- Explanation for selection

---

 Sample Input 2

 Java Developers

 ## Sample Output

 No suitable candidates found

 ---

## Demo video

https://drive.google.com/file/d/1W_Z6Qaer3li9YqwvfHVJkE74bsurNLOF/view?usp=drive_link

---

##  Tech Stack

- Backend: Python (Flask)
- Frontend: HTML
- Data: JSON
- Tools: VS Code, GitHub

---

## Future Improvements

- Real-time candidate database integration
- Advanced NLP for JD parsing
- Real conversational chatbot instead of simulation
- Authentication and recruiter dashboard

---

## Author

Rakshitha Dorairaj