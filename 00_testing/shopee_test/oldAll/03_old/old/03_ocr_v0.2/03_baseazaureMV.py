import os
import azure.ai.vision as sdk

# exported to environment variable, safer and more secure for sensitive information like APIs
VISION_ENDPOINT = os.environ.get("VISION_ENDPOINT")
VISION_KEY = os.environ.get("VISION_KEY")

if VISION_ENDPOINT is None or VISION_KEY is None:
    raise ValueError("VISION_ENDPOINT and VISION_KEY must be set in the environment")

service_options = sdk.VisionServiceOptions(VISION_ENDPOINT, VISION_KEY)

# Replace this with the path to your local image file
image_path = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\02_company.jpg'

# Read image content and create an image buffer
with open(image_path, 'rb') as image_file:
    image_buffer = image_file.read()

image_source_buffer = sdk.ImageSourceBuffer()
image_source_buffer.image_writer.write(image_buffer)
vision_source = sdk.VisionSource(image_source_buffer=image_source_buffer)

analysis_options = sdk.ImageAnalysisOptions()

analysis_options.features = (
    sdk.ImageAnalysisFeature.CAPTION |
    sdk.ImageAnalysisFeature.TEXT
)

analysis_options.language = "en"
analysis_options.gender_neutral_caption = False

image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

result = image_analyzer.analyze()

# Create a string to store the extracted information
extracted_info = ""

if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:
    if result.caption is not None:
        extracted_info += f"Caption: {result.caption.content}, Confidence: {result.caption.confidence}\n"

    if result.text is not None:
        extracted_info += "Text:\n"
        for line in result.text.lines:
            points_string = "{" + ", ".join([str(int(point)) for point in line.bounding_polygon]) + "}"
            extracted_info += f"  Line: {line.content}, Bounding polygon {points_string}\n"
            for word in line.words:
                points_string = "{" + ", ".join([str(int(point)) for point in word.bounding_polygon]) + "}"
                extracted_info += f"    Word: {word.content}, Bounding polygon {points_string}, Confidence: {word.confidence}\n"

# Save the extracted information to a text file
output_file_path = 'extracted_info.txt'
with open(output_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(extracted_info)

print("Extraction completed. Check 'extracted_info.txt' for the results.")