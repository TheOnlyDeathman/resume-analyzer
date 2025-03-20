import spacy

nlp = spacy.load("en_core_web_sm")

def parse_job_description(jd_text):
    doc = nlp(jd_text)
    skills = [token.text for token in doc if token.pos_ == "NOUN"]
    return set(skills)