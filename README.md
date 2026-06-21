# 📄 File Converter Pro
## 🌐 Try It Live

**[Click here to use File Converter Pro](https://file-converter-337s.onrender.com/)** - No installation needed!

A simple yet powerful web application to convert and manipulate files effortlessly. Convert JPG images to PDF, Word documents, merge PDFs, and more—all in one place!

![Flask](https://img.shields.io/badge/Flask-2.3+-blue?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## ✨ Features

- **JPG → PDF Conversion** - Convert single or multiple JPG images to a PDF file with batch support
- **JPG → Word Conversion** - Embed images directly into Word (.docx) documents
- **PDF Merge** - Combine multiple PDF files into a single document
- **PDF → JPG Conversion** - Extract images from PDF files
- **Batch Processing** - Handle multiple files at once
- **Fast & Lightweight** - Built with Flask for optimal performance
- **Responsive UI** - Beautiful Bootstrap-based interface that works on all devices
- **No Installation Required** - Use directly from the web browser

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/priyanshusingh205/File-Converter.git
   cd File-Converter
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:10000
   ```

---

## 📖 Usage

### Convert JPG to PDF
1. Go to the **JPG → PDF** section
2. Select one or multiple JPG files
3. Click **Convert**
4. Download your PDF automatically

### Convert JPG to Word
1. Go to the **JPG → Word** section
2. Select a JPG image
3. Click **Convert**
4. Download the Word document (.docx)

### Merge PDFs
1. Go to the **Merge PDF** section
2. Upload multiple PDF files
3. Click **Merge**
4. Download the combined PDF

### Convert PDF to JPG
1. Go to the **PDF → JPG** section
2. Select a PDF file
3. Click **Convert**
4. Download extracted images

---

## 🏗️ Project Structure

```
File-Converter/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Temporary file storage
├── README.md             # Documentation
└── .gitignore            # Git ignore file
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Flask** | Web framework |
| **Pillow** | Image processing |
| **PyPDF2** | PDF manipulation |
| **python-docx** | Word document creation |
| **Bootstrap 5** | Responsive UI |

---

## 🌐 Deployment

### Deploy on Heroku (Free Tier)

1. **Install Heroku CLI**
   ```bash
   # Visit: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a Procfile**
   ```bash
   echo "web: gunicorn app:app" > Procfile
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Deploy on PythonAnywhere
1. Create account at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload your code
3. Configure a web app with Flask
4. Reload and access your live URL

### Deploy on Render
1. Create account at [Render](https://render.com/)
2. Connect your GitHub repository
3. Configure build and start commands
4. Deploy automatically

---

## 💡 How It Works

### Image to PDF Conversion
```python
# Converts JPG/PNG images to RGB and saves as PDF
image.convert('RGB')
image.save(output, save_all=True, append_images=images[1:])
```

### Image to Word
```python
# Embeds images into .docx documents
doc = Document()
doc.add_picture(image_path)
doc.save(output_path)
```

### PDF Merge
```python
# Combines multiple PDFs into one
merger = PdfMerger()
merger.append(pdf_path)
merger.write(output_path)
```

---

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main page |
| `/convert_to_pdf` | POST | Convert JPG to PDF |
| `/convert_to_word` | POST | Convert JPG to DOCX |
| `/merge_pdf` | POST | Merge multiple PDFs |
| `/pdf_to_jpg` | POST | Convert PDF to JPG |

---

## 🐛 Known Limitations

- Maximum file size: 100MB per file (configurable)
- PDF → JPG conversion needs to be implemented
- Temporary files are stored in `uploads/` folder (cleanup recommended)
- Single instance deployment (consider scaling for production)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Priyanshu Singh**
- GitHub: [@priyanshusingh205](https://github.com/priyanshusingh205)

---

## ⭐ Support

If you find this project helpful, please consider:
- ⭐ **Starring the repository**
- 🐛 **Reporting issues** you encounter
- 💡 **Suggesting improvements**
- 🔗 **Sharing with others**

---

**Last Updated**: 2026  
**Status**: ✅ Active & Maintained
