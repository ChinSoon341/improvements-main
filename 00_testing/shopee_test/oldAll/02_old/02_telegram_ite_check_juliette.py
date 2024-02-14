import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import asyncio
from datetime import datetime

# ANSI escape codes for text colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

# Specify the path to your OneDrive folder
ONE_DRIVE_FOLDER = r'C:\Users\chinsoont.BECKHOFF\OneDrive - Singapore Polytechnic'

# Telegram bot token
TELEGRAM_BOT_TOKEN = '6540947414:AAGVoA9X-vw-Uq1b1YqLvTH8YkQX1UlfNkU'
DEFAULT_CHAT_ID = '1471225821'  # Replace with your default chat ID
OTHER_CHAT_ID = '1471225821'  # Replace with another chat ID

async def notify_on_telegram(search_term, status_text, awarded_to, award_value, award_date, recipient_chat_id=None):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # If recipient_chat_id is None, use the default chat ID
    chat_id = recipient_chat_id if recipient_chat_id else DEFAULT_CHAT_ID

    # Message formatting for better clarity (e.g., bolding the status_text)
    message = f"Status update for tender {search_term}:\n\n<b>{status_text}</b>\n\nAwarded to: {awarded_to}\nAward Value: {award_value}\nAward Date: {award_date}\n\nLast Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Use parse_mode='HTML' to enable text formatting (e.g., bold)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')

async def search_and_display(search_term):

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

    checkbox_title = driver.find_element(By.ID, 'contentForm:j_id55_0')
    checkbox_title.click()

    # Find the search input field and submit a query
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="contentForm:searchBar_searchBar_INPUT-SEARCH"]')
    search_input.send_keys(search_term)
    search_input.send_keys(Keys.RETURN)

    # Wait for a few seconds to let the search results load (you might need to adjust the wait time)
    time.sleep(0.5)

    wait = WebDriverWait(driver, 10)

    try:
        # Using XPath to locate the status element based on its class
        status_element = wait.until(EC.presence_of_element_located((
                By.XPATH, 
            '//div[@class="label_MAIN label_WHITE-ON-GRAY" or '
            '(@class="label_MAIN label_WHITE-ON-GREEN" and text()="AWARDED") or '
            '(@class="label_MAIN label_WHITE-ON-GRAY" and text()="OPEN") or '
            '(@class="label_MAIN label_WHITE-ON-LIGHT-GRAY" and (text()="CLOSED" or '
            'text()="CANCELLED" or text()="NO AWARD"))]'
        )))

        # Check if all elements are found
        status_text = status_element.text.strip()

        # Replace "\n" with a space in the output
        status_text = status_text.replace("\n", " ")

        # Using XPath to locate the additional elements for Awarded To, Award Value, and Award Date
        subtitle_elements = wait.until(EC.presence_of_all_elements_located((
            By.XPATH,
            "//div[@class='formOutputText_HIDDEN-LABEL outputText_SUBTITLE-BLACK' and @style='text-align: left;']"
        )))

        # Initialize variables for Awarded To, Award Value, and Award Date
        awarded_to = None
        award_value = None
        award_date = None

        # Loop through subtitle elements to dynamically assign values to columns
        for index, subtitle_element in enumerate(subtitle_elements):
            text = subtitle_element.text.strip()

            if index == 0:
                awarded_to = text
            elif index == 1:
                award_value = text
            elif index == 2:
                award_date = text

        # Notify on Telegram to the default chat ID
        await notify_on_telegram(search_term, status_text, awarded_to, award_value, award_date)

        # Notify on Telegram to another chat ID
        await notify_on_telegram(search_term, status_text, awarded_to, award_value, award_date, OTHER_CHAT_ID)

    except Exception as e:
        print(f"{COLOR_RED}An error occurred: {e}{COLOR_RESET}")

    # Close the browser
    driver.quit()

def start_telegram_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

def start_menu():
    asyncio.run(search_and_display("ITE000ETQ23000193"))

if __name__ == "__main__":
    start_menu()
