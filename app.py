import streamlit as st
from ocr_processing import ocr_image


def main():
    st.title("OCR Document Search Web App")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Call the OCR function
        extracted_text = ocr_image(uploaded_file)

        # Display the extracted text
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Add keyword search functionality if needed...


if __name__ == "__main__":
    main()
