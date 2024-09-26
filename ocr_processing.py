import easyocr

def ocr_image(image):
    reader = easyocr.Reader(['en', 'hi'])  # Specify the languages you want to use
    results = reader.readtext(image, detail=0)  # Extract text
    extracted_text = ' '.join(results)  # Join the results into a single string
    return extracted_text
