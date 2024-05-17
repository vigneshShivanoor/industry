import pdfplumber
import re

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_director_info(text):
    # Define the regular expression pattern
    pattern = r'(?:Dr\.|Mr\.|Mrs\.|Prof\.)\s+[A-Za-z]+ [A-Za-z]+ \(DIN: \d+\),\s+as\s+(?:Independent|Executive|managing) Director'
    
    # Find all matches in the text
    director_matches = re.findall(pattern, text)

    for director_info in director_matches:
        print(director_info)

# Path to the PDF file
pdf_file_path = 'D:/everythingfromc/si/data/Vinati.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Extract and print director information
extract_director_info(pdf_text)
