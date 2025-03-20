import openai

openai.api_key = "YOUR_OPENAI_AI_KEY"

def get_resume_feedback(resume_text, jd_text):
    prompt = f"Analyze this resume:\n{resume_text}\n\nagainst this job description:\n{jd_text}\n\nsuggest improvements."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response['choices'][0]['messages']['content']