import requests

url = "http://127.0.0.1:8000/analyze"
data = {
    "resume_path": "resume.pdf",
    "job_description": "Software Engineer with Python skills"
}

response = requests.post(url, json=data)

# Debugging: Print raw response
print("Status Code:", response.status_code)
print("Raw Response:", response.text)  # <-- This will show the actual response

try:
    print("Response JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Error: Response is not JSON formatted")