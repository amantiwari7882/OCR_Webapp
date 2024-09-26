import streamlit as st
from ocr_processing import ocr_image
from PIL import Image

st.title("OCR and Document Search Web App")

# Image uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR
    st.write("Extracting text...")
    extracted_text = ocr_image(image)

    # Display extracted text
    st.text_area("Extracted Text", extracted_text)

    # Search functionality
    search_query = st.text_input("Enter keyword to search")

    if search_query:
        if search_query.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_query}' found in the text.")
        else:
            st.write(f"Keyword '{search_query}' not found.")
