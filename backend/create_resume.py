from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_resume(pdf_path="resume.pdf"):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "John Doe")
    c.drawString(100, 735, "Software Engineer")
    c.drawString(100, 720, "Email: johndoe@example.com")
    c.drawString(100, 705, "Phone: +1 234 567 8901")
    c.drawString(100, 690, "---------------------------------------------")
    c.drawString(100, 675, "Skills:")
    c.drawString(120, 660, "- Python, Java, C++")
    c.drawString(120, 645, "- Machine Learning, NLP")
    c.drawString(120, 630, "- Web Development (Flask, Django)")
    c.drawString(100, 615, "---------------------------------------------")
    c.drawString(100, 600, "Experience:")
    c.drawString(120, 585, "- Software Engineer at XYZ Corp (2022 - Present)")
    c.drawString(120, 570, "- Intern at ABC Tech (2021 - 2022)")
    c.drawString(100, 555, "---------------------------------------------")

    c.save()
    print(f"Sample resume created at: {pdf_path}")

# Call the function to create the PDF
create_sample_resume()
