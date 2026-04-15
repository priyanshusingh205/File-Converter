from flask import Flask, render_template, request, send_file
from PIL import Image
from docx import Document
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

# JPG → PDF
@app.route('/convert_to_pdf', methods=['POST'])
def convert_to_pdf():
    files = request.files.getlist('files')
    image_list = []

    for file in files:
        if file.filename == "":
            continue

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        try:
            img = Image.open(path)

            if img.mode != 'RGB':
                img = img.convert('RGB')

            image_list.append(img)

        except Exception as e:
            return f"Error: {str(e)}"

    if not image_list:
        return "No valid images uploaded."

    pdf_path = os.path.join(UPLOAD_FOLDER, "output.pdf")
    image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])

    return send_file(pdf_path, as_attachment=True)


# JPG → WORD
@app.route('/convert_to_word', methods=['POST'])
def convert_to_word():
    file = request.files['file']

    if file.filename == "":
        return "No file selected"

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc = Document()
    doc.add_paragraph("Image inserted below:")
    doc.add_picture(path)

    doc_path = os.path.join(UPLOAD_FOLDER, "output.docx")
    doc.save(doc_path)

    return send_file(doc_path, as_attachment=True)


# 🔥 PDF → JPG
@app.route('/pdf_to_jpg', methods=['POST'])
def pdf_to_jpg():
    from pdf2image import convert_from_path

    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    images = convert_from_path(path)

    image_path = os.path.join(UPLOAD_FOLDER, "output.jpg")
    images[0].save(image_path, 'JPEG')

    return send_file(image_path, as_attachment=True)


# 🔥 WORD → PDF
@app.route('/word_to_pdf', methods=['POST'])
def word_to_pdf():
    from fpdf import FPDF

    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc = Document(path)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    pdf_path = os.path.join(UPLOAD_FOLDER, "output.pdf")
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)