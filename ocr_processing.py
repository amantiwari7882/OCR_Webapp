import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image):
    """Process an image and extract text using pytesseract"""
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')  # For English and Hindi
    return extracted_text
