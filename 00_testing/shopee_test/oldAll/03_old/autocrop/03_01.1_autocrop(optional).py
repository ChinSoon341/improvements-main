from PIL import Image
import os

def auto_crop_and_pad(input_folder, output_folder, y_start):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all JPEG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            # Construct the full path to the input image
            input_path = os.path.join(input_folder, filename)

            # Open the image
            img = Image.open(input_path)

            # Get the dimensions of the image
            width, height = img.size

            # Set the crop box
            box = (0, y_start, width, height)

            # Crop the image
            cropped_img = img.crop(box)

            # Calculate the amount of black padding needed at the bottom
            padding_height = height - y_start

            # Create a new image with black padding at the bottom
            padded_img = Image.new("RGB", (width, height), color="black")
            padded_img.paste(cropped_img, (0, 0))

            # Save the result to the output folder
            output_path = os.path.join(output_folder, filename)
            padded_img.save(output_path)

if __name__ == "__main__":
    # Specify the input and output folders
    input_folder = r"C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\example"
    output_folder = r"C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\example"

    # Specify the Y_start position for cropping
    y_start = 282  # Adjust this value as needed

    # Perform auto cropping and padding
    auto_crop_and_pad(input_folder, output_folder, y_start)
