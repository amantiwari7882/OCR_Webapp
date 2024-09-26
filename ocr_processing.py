import easyocr
import numpy as np
from PIL import Image
import io

def ocr_image(uploaded_file):
    # Read the uploaded file as a PIL Image
    image = Image.open(uploaded_file)

    # Convert the image to an array
    image_np = np.array(image)

    # Initialize EasyOCR Reader
    reader = easyocr.Reader(['en', 'hi'])  # Specify the languages you want to use

    # Read text from the image
    results = reader.readtext(image_np, detail=0)  # Extract text
    extracted_text = ' '.join(results)  # Join the results into a single string
    return extracted_text
