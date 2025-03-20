from flask import Flask, send_file
import os
from create_resume import create_sample_resume  # Import the resume creation function

app = Flask(__name__)

# Define the correct path to resume.pdf inside the backend directory
RESUME_PATH = os.path.join(os.getcwd(), "resume.pdf")

@app.route("/download-resume")
def download_resume():
    # Ensure the resume exists before sending
    if not os.path.exists(RESUME_PATH):
        create_sample_resume(RESUME_PATH)  # Create the resume if not found

    return send_file(RESUME_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector  # MySQL connector

app = Flask(__name__)
CORS(app)

# 🔹 Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",      # Change if your MySQL is hosted remotely
    user="root",           # Your MySQL username
    password="yourpassword",  # Your MySQL password
    database="resume_analyzer"  # Your database name
)

cursor = db.cursor()

