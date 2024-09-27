import pytesseract
from PIL import Image
import streamlit as st

# Image upload and OCR function
def ocr_image(image):
    return pytesseract.image_to_string(image, lang='eng+hin')

# Web app
st.title("OCR and Document Search")
uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    extracted_text = ocr_image(image)
    st.text_area("Extracted Text", extracted_text)

    search_query = st.text_input("Search Keywords")
    if search_query:
        if search_query.lower() in extracted_text.lower():
            st.write(f"Found '{search_query}' in the text!")
        else:
            st.write("No matches found.")
