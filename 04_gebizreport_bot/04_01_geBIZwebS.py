import os #interacting with the operating system
from selenium import webdriver  # web browser automation
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time #delays in the script
import asyncio #asynchronous programming
from datetime import datetime #manipulating date and time objects

# ANSI escape codes for text colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

def search_and_display(search_term): #function takes a search_term as input. It sets up an event loop using asyncio
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

        checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_1') #section finds specific elements on the webpage using Selenium's find_element method and interacts with them (e.g., clicking checkboxes, entering search terms)
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


        try:
            for page_number in range(1, 11): # section iterates through 10 pages of search results, waiting for elements to load, writing them to files, and clicking the "Next" button to navigate to the next page
                # Using WebDriverWait to wait for the presence of the div elements with common structure
                div_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-md-12 ']")))

                with open(f'C:\\Users\\ADAM7\\Desktop\\Projects_demo\\04_gebizReport\\temp\\p{page_number}.txt', 'w', encoding='utf-8') as output_file: # writes the text content of certain elements to text files, organized by page number
                    for div_element in div_elements:
                        # Extract the text content of each matching element
                        div_text = div_element.text

                        # Process div_text as needed

                        output_file.write(f"{div_text}\n")

                print(f"page {page_number} done")

                time.sleep(2.5)

                # Locate the next button
                next_button_xpath = '//input[contains(@id, "contentForm:j_idt912:j_idt963_Next_")]'
                next_button = driver.find_element(By.XPATH, next_button_xpath)

                # Click the next button
                next_button.click()

                time.sleep(2.5)

        except Exception as e:
            print(f"{COLOR_RED}An error occurred: {e}{COLOR_RESET}")

        # Close the browser
        driver.quit()

    loop.run_until_complete(asyncio.to_thread(run_in_executor))

def start_menu():
    keyTerm = "car" #define keywords in GeBIZ
    search_and_display(keyTerm) # function serves as the entry point to the script. It defines a keyTerm (presumably the search term) and calls the search_and_display function with this term
    
if __name__ == "__main__":
    start_menu()
