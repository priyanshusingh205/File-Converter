from flask import Flask, render_template, request, send_file
from PIL import Image
from docx import Document
from PyPDF2 import PdfMerger
from pdf2image import convert_from_path
import os
import time

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
    base_name = files[0].filename.split('.')[0]

    images = []
    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)

    output = os.path.join(UPLOAD_FOLDER, base_name + ".pdf")
    images[0].save(output, save_all=True, append_images=images[1:])

    return send_file(output, as_attachment=True)


# JPG → WORD
@app.route('/convert_to_word', methods=['POST'])
def convert_to_word():
    file = request.files['file']
    base_name = file.filename.split('.')[0]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc = Document()
    doc.add_picture(path)

    output = os.path.join(UPLOAD_FOLDER, base_name + ".docx")
    doc.save(output)

    return send_file(output, as_attachment=True)


# MERGE PDF
@app.route('/merge_pdf', methods=['POST'])
def merge_pdf():
    files = request.files.getlist('files')
    merger = PdfMerger()

    base_name = str(int(time.time()))

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        merger.append(path)

    output = os.path.join(UPLOAD_FOLDER, base_name + "_merged.pdf")
    merger.write(output)
    merger.close()

    return send_file(output, as_attachment=True)


# PDF → JPG
@app.route('/pdf_to_jpg', methods=['POST'])
def pdf_to_jpg():
    file = request.files['file']
    base_name = file.filename.split('.')[0]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    images = convert_from_path(path)

    output = os.path.join(UPLOAD_FOLDER, base_name + ".jpg")
    images[0].save(output, "JPEG")

    return send_file(output, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)