import pdfplumber
import docx

def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def parse_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def parse_document(file_path):
    file_extension = file_path.split('.')[-1].lower()
    if file_extension == 'pdf':
        return parse_pdf(file_path)
    elif file_extension == 'docx':
        return parse_docx(file_path)
    elif file_extension == 'txt':
        return parse_txt(file_path)
    else:
        raise ValueError("Unsupported file format.")