# OCR and Document Search Web Application

This is a simple web-based application that allows users to upload an image, extract text using Optical Character Recognition (OCR), and perform keyword searches on the extracted text. The application is built using Python, Pytesseract, and Streamlit for the web interface.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Assumptions](#assumptions)
- [Technologies Used](#technologies-used)

---

## Project Overview
This project demonstrates the ability to:
- Perform OCR on an uploaded image that contains text in both **Hindi** and **English**.
- Extract text from the image using the `pytesseract` library.
- Allow users to enter keywords to search within the extracted text.
- Highlight and return the search results directly on the web page.

---

## Features
1. **Image Upload**: Users can upload an image in common formats such as JPEG, PNG, etc.
2. **Text Extraction**: The app uses Tesseract to extract text in both English and Hindi from the uploaded image.
3. **Keyword Search**: Users can search for specific keywords within the extracted text, with the results displayed directly on the same page.
4. **Simple UI**: The interface is built with Streamlit, providing an easy-to-use, intuitive web interface.

---

## Installation

### Prerequisites
- **Python 3.8+**
- **Tesseract OCR**: You need to install Tesseract OCR on your system. Follow the instructions below based on your operating system:

#### **Windows**:
1. Download Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install it, and add the installation directory (e.g., `C:\Program Files\Tesseract-OCR\`) to your system's PATH environment variable.

#### **macOS**:
```bash
brew install tesseract
```

#### **Linux**:
```bash
sudo apt-get install tesseract-ocr
```

### Step-by-Step Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up the Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Tesseract Installation**:
   Ensure that Tesseract is installed and available in your system PATH. You can verify this by running:
   ```bash
   tesseract --version
   ```

---

## Usage

1. **Run the Web Application**:
   ```bash
   streamlit run app.py
   ```
   This will start the Streamlit web server. The app will be available at `http://localhost:8501` in your web browser.

2. **Upload an Image**:
   - On the web page, upload an image (JPEG, PNG) containing text in both Hindi and English.
   - The application will display the uploaded image and extract text from it.

3. **Search for Keywords**:
   - After extracting text, enter a keyword in the search box.
   - The app will search the extracted text and inform whether the keyword is found or not.

---

## Deployment

You can deploy the app on any platform that supports Streamlit, such as **Streamlit Sharing** or **Hugging Face Spaces**.

### Deploy on Streamlit Sharing:
1. Push your project to GitHub.
2. Go to [Streamlit Sharing](https://streamlit.io/sharing) and connect your GitHub repository.
3. Select the repository and branch, and deploy the app.

Alternatively, you can deploy the app on **Hugging Face Spaces** following similar steps.

---

## Assumptions
- The images uploaded contain clear, readable text in both English and Hindi.
- Tesseract OCR is capable of handling these languages effectively.
- The application currently supports searching for a single keyword at a time.

---

## Technologies Used
- **Python 3.8+**: The programming language used to build the backend of the application.
- **Streamlit**: A Python-based web framework for creating web applications.
- **Pytesseract**: A Python wrapper for the Tesseract OCR engine.
- **Tesseract**: An open-source OCR engine used to extract text from images.
- **Pillow**: A Python Imaging Library to handle image uploads and manipulations.

---

## Troubleshooting

1. **TesseractNotFoundError**:
   If you see the error `TesseractNotFoundError: tesseract is not installed or it's not in your PATH`, ensure Tesseract is installed and properly added to your system's PATH environment variable. You can explicitly set the path in your code:
   ```python
   import pytesseract
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

2. **Streamlit not opening in the browser**:
   Make sure you're running the app using:
   ```bash
   streamlit run app.py
   ```

---

## Conclusion

This project demonstrates how to build a web-based OCR and search tool for handling both English and Hindi text in images. The app is lightweight, user-friendly, and easy to deploy on any platform that supports Python and Streamlit.
