from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Import the By class

from bs4 import BeautifulSoup
import time

# Set the path to your webdriver (replace with the actual path to your chromedriver.exe)
webdriver_path =r'C:\Users\chinsoont.BECKHOFF\Downloads'

# Set the webdriver path using the executable_path argument
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--webdriver={webdriver_path}')
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.gebiz.gov.sg/'

# Open the website in the browser
driver.get(url)

# Wait for a few seconds to let the page load (you might need to adjust the wait time)
time.sleep(2)

checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_2') #selects the Agency
checkbox_title.click()
checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_3') #selects the Procurement Category 
checkbox_title.click()
checkbox_title = driver.find_element(By.ID, 'contentForm:j_id56_1') #select Match Any 
checkbox_title.click()

# Find the search input field and submit a query
#search_input = driver.find_element_by_name('contentForm:searchBar_searchBar_INPUT-SEARCH')  # Replace with the actual input name
search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="contentForm:searchBar_searchBar_INPUT-SEARCH"]')
search_input.send_keys('machinery, warehouse, ether CAT, automation, smart manufacturing, PLC, IPC')
search_input.send_keys(Keys.RETURN)

# Wait for a few seconds to let the search results load (you might need to adjust the wait time)
time.sleep(5)

# Get the HTML content of the current page after the search
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract information based on the HTML structure
# For example, print the text content of all h2 elements on the page
for h2_element in soup.find_all('h2'):
    print(h2_element.text.strip())
