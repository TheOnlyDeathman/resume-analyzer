# 🤖 AI Resume Analyzer for Machine Learning Jobs

This project analyzes a candidate's resume against a given job description using the OpenAI API. It provides machine learning (ML)-focused feedback including keyword suggestions, missing technical skills, and recommendations for improvement.

⚠️ **Note:** This is an initial/basic version of the model and not the most optimized or efficient version. Future updates will include more advanced features, better resume parsing, and performance improvements.

## 🧠 Project Overview

The AI Resume Analyzer is designed to help applicants in Machine Learning roles enhance their resumes by identifying:
- Missing ML-specific keywords
- Tools and technologies to highlight (e.g., TensorFlow, PyTorch, scikit-learn)
- Suggestions to improve experience descriptions
- Overall alignment score with the job description

#📽️ Demo Video

👉 [Watch the Demo Output]1.(https://drive.google.com/file/d/1LGxJWZsy0Yez3NY1WdMVDenY17yI6Nvv/view?usp=drivesdk)
                           2.(https://drive.google.com/file/d/1LGmebPWGYV8mYsy-oXE5COJ2yjzfhKpq/view?usp=drivesdk)
## 📂 Project Structure

```plaintext
resume-analyzer/
├── .env                  # API key storage
├── app_suggestions.py    # Core logic for resume feedback
├── resume.txt            # Sample resume text
├── job_description.txt   # Sample job description
├── resume_analysis_output.mp4  # Screen recording of output
├── requirements.txt      # Dependencies
└── README.md             # This file
