import subprocess
import os
def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    print(f"Running {script_name}")
    subprocess.run(["python", script_path])
if __name__ == "__main__":
    run_script("03_01_pdfconverted.py")
    run_script("03_02_reordercombined.py")
    run_script("03_03_checkbox.py")
    run_script("03_03.2_checkbox_cropbigger.py")
    run_script("03_04_ocr.py")
