# OCR Web Application

This project demonstrates an OCR (Optical Character Recognition) web application that processes images containing text in both Hindi and English languages. The application extracts text from the uploaded images and allows users to search for specific keywords within the extracted text.

## Features
- Upload images in common formats (JPEG, PNG, etc.).
- Extract text in both **Hindi** and **English** from the uploaded images using OCR.
- Search for specific keywords in the extracted text and display the matching results.
- Simple, user-friendly interface.
- Deployed on Hugging Face Spaces using Streamlit.

## Tech Stack
- **Python**: Core programming language for developing the application.
- **Streamlit**: Web framework for building and deploying the app interface.
- **Tesseract OCR**: Open-source OCR engine for text extraction.
- **Pytesseract**: Python wrapper for Tesseract OCR.
- **Transformers and PyTorch**: For enhanced OCR model integration (if applicable).

## Setup and Installation

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amantiwari7882/OCR_Webapp.git
   cd OCR_Webapp
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract**:
   - On Windows, download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - On Linux (for example, Ubuntu), run the following command:
     ```bash
     sudo apt install tesseract-ocr
     ```

5. **Run the Application**:
   Launch the Streamlit app locally using the following command:
   ```bash
   streamlit run app.py
   ```

6. **Visit the Web Interface**:
   Once the app is running, open your browser and navigate to `http://localhost:8501` to use the application.

### Deployment to Hugging Face Spaces

To deploy the app to Hugging Face Spaces, follow these steps:

1. **Create a Space** on Hugging Face with the SDK set to **Streamlit**.
2. **Push your code** to the Hugging Face Space repository:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push origin main
   ```
3. Hugging Face Spaces will automatically build and deploy the application.

## Usage
- Upload an image containing Hindi and/or English text.
- Click the **Extract Text** button to run OCR on the image.
- Once the text is extracted, you can enter a keyword in the search bar and click **Search** to find the occurrences of that word in the extracted text.
  
## Example

1. Upload an image (for example, a signboard with Hindi and English text).
2. The application will extract text, which might look like this:
   ```text
   "Welcome to the store. स्वागत है।"
   ```
3. Search for the keyword "store" or "स्वागत" to highlight it in the extracted text.

## Project Structure

```
OCR_Webapp/
│
├── app.py               # Main application file for Streamlit
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── .gitignore           # Files to ignore in version control
```

## Dependencies

- `streamlit`: For building the web interface.
- `pytesseract`: For performing OCR.
- `Pillow`: For image processing.
- `transformers` and `torch`: For advanced OCR model integrations.
- `opencv-python`: For handling image operations.

## Future Improvements
- Enhance the OCR accuracy for multi-language support.
- Add support for more image formats.
- Implement batch processing of multiple images.

---
