import streamlit as st
import requests

st.title("AI Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)")
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file is not None and job_description:
        files = {"resume": uploaded_file}
        response = requests.post("http://12.0.0.1:5000/analyze",json={"resume_path": uploaded_file.name, "job_description": job_description})
        
        if response.status_code == 200:
            result = response.json()
            st.write(f"**Match Score:** {result['match_score'] * 100:.2f}%")
            st.write(f"**Suggestions:** {result['feedback']}")
        else:
            st.warning("Please upload a resume and enter a job description.")