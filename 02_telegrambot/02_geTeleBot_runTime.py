import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import re

TELEGRAM_BOT_TOKEN = '6540947414:AAGVoA9X-vw-Uq1b1YqLvTH8YkQX1UlfNkU'
DEFAULT_CHAT_ID = '1471225821'  # Replace with your default chat ID
OTHER_CHAT_ID = '1471225821'  # Replace with another chat ID

# Function to validate the tender number
def validate_tender_number(tender_number):
    # Check if the tender number has exactly 17 characters
    if len(tender_number) != 17:
        return False
    # Check if the tender number starts with 3 letters
    if not tender_number[:3].isalpha():
        return False
    # Check if the tender number follows the pattern of 3 letters followed by 14 alphanumeric characters
    if not re.match(r'^[a-zA-Z]{3}\w{14}$', tender_number):
        return False
    return True

# Define the function to display the custom keyboard
def show_keyboard(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Change Tender Number", callback_data='change_tender')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select an option:', reply_markup=reply_markup)

# Define the button callback function
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'change_tender':
        query.message.reply_text('Please enter the new tender number:')

# Define a function to handle incoming messages for changing the tender number
def handle_tender_message(update: Update, context: CallbackContext) -> None:
    tender_number = update.message.text
    if validate_tender_number(tender_number):
        log_file_path = r'C:\Users\ADAM7\Desktop\Projects_demo\02_telegrambot\app_data\tenderNo.txt'
        with open(log_file_path, 'w') as file:
            file.write(tender_number)
        update.message.reply_text(f'Thank you! Tender number {tender_number} has been stored.')
    else:
        update.message.reply_text('The tender number you entered is not valid. Please enter again.')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handler for /settings
    dp.add_handler(CommandHandler("admin", show_keyboard))
    
    # Register button callback handler
    dp.add_handler(CallbackQueryHandler(button))

    # Register message handler for changing the tender number
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_tender_message))
    
    # Register a catch-all handler for any other messages
    dp.add_handler(MessageHandler(Filters.all, show_keyboard))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
