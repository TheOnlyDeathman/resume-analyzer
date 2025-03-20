from flask import Flask, request, jsonify
from resume_parser import extract_text_from_pdf
from job_parser import parse_job_description
from matcher import calculate_similarity
from ai_suggestions import get_resume_feedback

app = Flask(__name__)

# Homepage Route to Prevent 404 Errors
@app.route('/')
def home():
    return "Flask App Running!"

# API Route for Analyzing Resumes
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data or 'resume_path' not in data or 'job_description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    resume_text = extract_text_from_pdf(data['resume_path'])
    jd_text = data['job_description']
    match_score = calculate_similarity(resume_text, jd_text)
    feedback = get_resume_feedback(resume_text, jd_text)

    return jsonify({"match_score": match_score, "feedback": feedback})

# Fix: Corrected the "__main__" check
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
