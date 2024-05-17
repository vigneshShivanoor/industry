from flask import Flask, render_template, request
import pdfplumber
import re

app = Flask(__name__)

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_director_detail(text):
    director_details = []
    director_patterns = r"\. (.+?) \(DIN: (\d+)\),\s+(.*?)\s+as\s+(.*?)(?=;|\n|$)"
    director_pattern = r"(Mr\.|Mrs\.|Ms\.|Dr\.)\s+([A-Za-z]{2,})"
    din_pattern = r"DIN:\s(\d+)"
    processed_directors = set()
    
    director_matches = re.findall(director_pattern, text)
    din_matches = re.findall(din_pattern, text)
    all_director_patterns = re.findall(director_patterns, text)
    
    for (director_name, din_number, role), director_match, din_match in zip(all_director_patterns, director_matches, din_matches):
        if director_name not in processed_directors:
           processed_directors.add(director_name)
           director_details.append({'director': director_name, 'din': din_match, 'role': role})

    
    return director_details

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('results.html', error='No file part')
    file = request.files['file']
    if file.filename == '':
        return render_template('results.html', error='No selected file')
    if file:
        text = extract_text_from_pdf(file)
        director_details = extract_director_detail(text)
        return render_template('results.html', director_details=director_details)

if __name__ == '__main__':
    app.run(debug=True)
