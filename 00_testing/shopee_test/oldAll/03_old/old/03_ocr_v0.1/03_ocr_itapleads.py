import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image (adjust the dimensions as needed)
    resized_image = cv2.resize(gray_image, (600, 800))

    return resized_image

def extract_text_with_lstm(image):
    # Use Tesseract with LSTM engine to extract text
    text = pytesseract.image_to_string(image, config='--psm 11 --oem 1', lang='eng')

    return text

# Path to your image
image_path = r'C:\Users\chinsoont.BECKHOFF\Documents\program\ocr\img_data\img=20.jpg'

# Preprocess the image
preprocessed_image = preprocess_image(image_path)

# Extract text using LSTM engine
full_text = extract_text_with_lstm(preprocessed_image)

# Print the raw OCR output
print("Raw OCR Output:", full_text)
