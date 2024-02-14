import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pyautogui

def search_and_capture(search_term):
    try:
        # Set the path to your chromedriver.exe
        webdriver_path = r'C:\Users\chinsoont.BECKHOFF\Downloads\chromedriver.exe'

        # Set the webdriver path using the executable_path argument
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Optional: run in headless mode
        chrome_options.add_argument(f'--webdriver={webdriver_path}')
        prefs = {'download.default_directory': r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic\improvements\04_geBIZ_report'}
        chrome_options.add_experimental_option('prefs', prefs)

        # Initialize the Chrome driver with options
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website in the browser
        driver.get('https://www.gebiz.gov.sg/')

        # Wait for a few seconds to let the page load (you might need to adjust the wait time)
        time.sleep(0.2)

        # Perform actions on the webpage
        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_1')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_2')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_3')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id56_1')
        checkbox_title.click()

        search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="contentForm:searchBar_searchBar_INPUT-SEARCH"]')
        search_input.send_keys(search_term)
        search_input.submit()

        time.sleep(0.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt800_TabAction_1")  # closed cat
        checkbox_title.click()

        time.sleep(0.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt905")  # awarded cat
        checkbox_title.click()

        time.sleep(0.5)

        # Use PyAutoGUI to simulate keyboard shortcuts for capturing a full-size screenshot
        pyautogui.hotkey('ctrl', 'shift', 'p')
        time.sleep(1)  # Adjust this sleep time based on the responsiveness of your system

        pyautogui.write("screenshot")
        time.sleep(1)

        pyautogui.press('enter')
        time.sleep(5)

    except Exception as e:
        print("Error:", str(e))
    finally:
        # Close the browser
        driver.quit()

# Example usage
search_and_capture("machinery, warehouse, ether CAT, automation, manufacturing, PLC, IPC")
