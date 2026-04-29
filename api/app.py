from flask import Flask, request, jsonify
from ai.resume_parser import extract_text
from ai.skill_matcher import match_skills
from ai.career_recommender import recommend_career

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Job Portal Running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']

    text = extract_text(file)
    result = match_skills(text)

    career = recommend_career(result["skills_found"])
    result["recommended_career"] = career

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)