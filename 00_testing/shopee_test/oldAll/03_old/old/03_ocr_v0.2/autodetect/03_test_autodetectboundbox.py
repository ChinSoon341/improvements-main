import cv2
import numpy as np
import os

def detect_blur(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the Laplacian of the image to get the intensity gradient
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Compute the variance of the Laplacian to measure the blur
    blur_variance = np.var(laplacian)

    return blur_variance

def crop_blur(image):
    blur_value = detect_blur(image)

    # Set a threshold for blur detection
    blur_threshold = 100  # Adjust this threshold as needed

    if blur_value > blur_threshold:
        # If blur detected, find the topmost blurred region and crop it out
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the topmost contour (assuming it's the blurred region)
            topmost_contour = min(contours, key=lambda c: cv2.boundingRect(c)[1])

            # Crop out the topmost blurred region
            x, y, w, h = cv2.boundingRect(topmost_contour)
            image = image[y+h:, :, :]

    return image

# Folder containing JPEG images
folder_path = r"C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr_raja\v0.2\dataset\trial\png_3detection"

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        # Construct the full path to the image
        image_path = os.path.join(folder_path, filename)

        # Read the image
        image = cv2.imread(image_path)

        # Crop out the blurred region if detected
        cropped_image = crop_blur(image)

        # Save the cropped image back to the same file
        cv2.imwrite(image_path, cropped_image)
