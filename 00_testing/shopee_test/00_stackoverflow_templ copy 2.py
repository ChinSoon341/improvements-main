from os.path import expanduser
from seleniumbase import BaseCase
from PIL import Image
import pytesseract
import re
from telegram import Bot

import asyncio

TELEGRAM_TOKEN = '6917913070:AAH5Mi16sMluGSmUL-5e1lw2eyuXueoJjx0'
CHAT_ID = '1471225821'
ADDITIONAL_CHAT_ID = '1147646447'


async def notify_on_telegram(message, chat_ids=None):
    if chat_ids is None:
        chat_ids = [CHAT_ID]

    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        formatted_message = f"<b>Shopee Product Information:</b>\n\n{message}"



        for chat_id in chat_ids:
            await bot.send_message(chat_id=chat_id, text=formatted_message, parse_mode='HTML')

        print("Message sent successfully to Telegram.")
    except Exception as e:
        print(f"Failed to send message to Telegram. Error: {e}")


class CDPTests(BaseCase):
    def test_display_cdp_events(self):
        if not self.undetectable or not self.uc_cdp_events:
            self.get_new_driver(undetectable=True, uc_cdp_events=True)

        self.open("https://shopee.sg/mall/search?keyword=iphone")

        # Wait for the page to load (you might need to adjust the time)
        self.sleep(2)

        # Get the path to the documents\storage\00_shopee_misc folder
        misc_folder_path = expanduser("~/Documents/storage/00_shopee_misc")

        # Take a screenshot and save it to the specified folder
        screenshot_path = f"{misc_folder_path}/iphomegimme.png"
        self.save_screenshot(screenshot_path)

        # Perform OCR on the screenshot with enhanced parameters
        extracted_text = self.perform_ocr(screenshot_path)

        # Extract all information from the OCR result
        extracted_info = self.extract_relevant_info(extracted_text)

        # Save extracted information to the text file in the specified folder
        text_file_path = f"{misc_folder_path}/extract_from_ocr.txt"
        with open(text_file_path, 'w') as file:
            file.write(extracted_info)

        # Send the relevant information to Telegram with both chat IDs
        asyncio.create_task(notify_on_telegram(extracted_info, chat_ids=[CHAT_ID, ADDITIONAL_CHAT_ID]))

    def perform_ocr(self, image_path):
        # Open the image using Pillow
        img = Image.open(image_path)

        # Use Tesseract to perform OCR with enhanced parameters
        extracted_text = pytesseract.image_to_string(img, config='--psm 11')

        return extracted_text
    
    def extract_relevant_info(self, text):
        # Use regular expressions to extract relevant information (product name and price)
        product_name_match = re.search(r'Apple iPhone [0-9]+ [^\n]+', text)
        price_match = re.search(r'\$\s*[0-9,.]+', text)

        product_name = product_name_match.group() if product_name_match else "Product Name Not Found"
        price = price_match.group() if price_match else "Price Not Found"

        return f"Product Name: {product_name}\nPrice: {price}"


if __name__ == "__main__":
    from pytest import main

    # Run SeleniumBase test using pytest
    main([__file__,"--headless", "--uc", "--uc-cdp", "--incognito", "-s"])

    # Get the path to the documents\storage\00_shopee_misc folder
    misc_folder_path = expanduser("~/Documents/storage/00_shopee_misc")

    # Read the extracted information from the text file in the specified folder
    with open(f"{misc_folder_path}/extract_from_ocr.txt", "r") as file:
        extracted_info = file.read()

    # Notify on Telegram with the extracted information to both chat IDs
    asyncio.run(notify_on_telegram(extracted_info, chat_ids=[CHAT_ID, ADDITIONAL_CHAT_ID]))
