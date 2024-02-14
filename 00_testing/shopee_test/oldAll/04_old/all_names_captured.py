import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import asyncio

# ANSI escape codes for text colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

def search_and_display(search_term):
    loop = asyncio.get_event_loop()

    def run_in_executor():
        # Set the path to your webdriver (replace with the actual path to your chromedriver.exe)
        webdriver_path = r'C:\Users\chinsoont.BECKHOFF\Downloads'

        # Set the webdriver path using the executable_path argument
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--webdriver={webdriver_path}')

        # Add the following line to run Chrome in headless mode
        # chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options)

        url = 'https://www.gebiz.gov.sg/'

        # Open the website in the browser
        driver.get(url)

        # Wait for a few seconds to let the page load (you might need to adjust the wait time)
        time.sleep(0.2)

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_1')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_2')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_3')
        checkbox_title.click()

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id56_1')
        checkbox_title.click()

        # Find the search input field and submit a query
        search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="contentForm:searchBar_searchBar_INPUT-SEARCH"]')
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

        # Wait for a few seconds to let the search results load (you might need to adjust the wait time)
        time.sleep(0.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt800_TabAction_1") #closed cat
        checkbox_title.click()

        time.sleep(1.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt905") #awarded cat
        checkbox_title.click()

        time.sleep(1.5)

        # Initialize an empty list to store the results
        results = []

        # Create WebDriverWait inside the function since it relies on the driver object
        wait = WebDriverWait(driver, 10)

        # Find all elements matching the XPath
        elements = driver.find_elements(By.XPATH, './/a[@class="commandLink_TITLE-BLUE"]')

        # Loop through the elements and append their text content to the results list
        for i, element in enumerate(elements):
            results.append(element.text)

        # Create a DataFrame with the results
        df = pd.DataFrame({"No.": range(1, len(elements) + 1), "Tender Name": results})

        # Write the DataFrame to an Excel file
        excel_file_path = 'output.xlsx'
        df.to_excel(excel_file_path, index=False)

        print(f"{COLOR_GREEN}Information extracted and saved to {excel_file_path}{COLOR_RESET}")

        # Close the browser
        driver.quit()

    loop.run_until_complete(asyncio.to_thread(run_in_executor))

def start_menu():
    search_and_display("machinery, warehouse, automation, manufacturing, PLC, IPC")

if __name__ == "__main__":
    start_menu()
