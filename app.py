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


# ✅ JPG → PDF
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


# ✅ JPG → WORD
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


# ✅ WORD → PDF (FIXED VERSION)
@app.route('/word_to_pdf', methods=['POST'])
def word_to_pdf():
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

    file = request.files['file']

    if file.filename == "":
        return "No file selected"

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    doc = Document(path)

    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    pdf_path = os.path.join(UPLOAD_FOLDER, "output.pdf")

    pdf = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    story = []
    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    pdf.build(story)

    return send_file(pdf_path, as_attachment=True)


# ❌ PDF → JPG (TEMP DISABLED — ERROR AATA HAI RENDER PE)
# Isko abhi use mat karo


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)