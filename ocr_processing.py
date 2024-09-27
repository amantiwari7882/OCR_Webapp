from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load the model and processor from Hugging Face
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Function to perform OCR using Hugging Face
def ocr_image(image_path):
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

# Example usage
image_path = 'path_to_image.jpg'
extracted_text = ocr_image(image_path)
print(extracted_text)
