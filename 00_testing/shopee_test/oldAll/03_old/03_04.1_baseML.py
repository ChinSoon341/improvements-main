import subprocess

def main():

    image_pth = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\Data_source\reorder\1_output\06_category_uncropped.jpg'

    # Replace the command with your desired one
    command = [
        'python', r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\detect.py',
        '--weights', r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\03_ocr\v1.0\yolov5\yolov5-master\runs\train\desktop_trained_model\weights\best.pt',
        '--img-size', '640',
        '--conf', '0.7',
        '--source', image_pth,
        '--save-txt',
        '--exist-ok'
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
