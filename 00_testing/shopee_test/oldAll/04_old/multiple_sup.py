import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import asyncio
from datetime import datetime

# ANSI escape codes for text colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
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
        #chrome_options.add_argument('--headless')

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
        time.sleep(2.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt800_TabAction_1") #closed cat
        checkbox_title.click()

        time.sleep(2.5)

        checkbox_title = driver.find_element(By.ID, "contentForm:j_idt905") #awarded cat
        checkbox_title.click()

        time.sleep(2.5)

        wait = WebDriverWait(driver, 10)

        next_button_xpath = '//input[contains(@id, "contentForm:j_idt912:j_idt963_Next_")]'

        for _ in range(10):
            time.sleep(2.5)
            # Find the element matching the XPath
            next_button = driver.find_element(By.XPATH, next_button_xpath)

            # Perform an action, e.g., click the button
            next_button.click()

            time.sleep(2.5)






        """
        # Assuming 'driver' is your WebDriver instance
        next_button_xpath = '//input[contains(@id, "contentForm:j_idt912:j_idt963_Next_")]'

        # Find the element matching the XPath
        next_button = driver.find_element(By.XPATH, next_button_xpath)

        # Perform an action, e.g., click the button
        next_button.click()
        """


        try:
            # Using XPath to locate the status element based on its class

            time.sleep(2.5)



            # Write the extracted information to a text file
            output_file_path = 'output.txt'
            with open(output_file_path, 'w') as output_file:
                output_file.write(status_text)

            print(f"{COLOR_GREEN}Information extracted and saved to {output_file_path}{COLOR_RESET}")

        except Exception as e:
            print(f"{COLOR_RED}An error occurred: {e}{COLOR_RESET}")

        # Close the browser
        driver.quit()

    loop.run_until_complete(asyncio.to_thread(run_in_executor))

def start_menu():
    search_and_display("machinery, warehouse, automation, manufacturing, PLC, IPC")

if __name__ == "__main__":
    start_menu()
