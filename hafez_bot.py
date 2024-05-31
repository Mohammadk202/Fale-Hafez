import openpyxl
import random
from telegram import Update, ForceReply, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the BOT_TOKEN from the environment
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

# Function to read poems and definitions from the XLSX file
def read_poems_from_xlsx(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    poems = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header row
        poem = row[1].replace("_x000D_", "").strip() if row[1] else ""
        meaning = row[2].replace("_x000D_", "").strip() if row[2] else ""
        poems.append((poem, meaning))
    return poems

# Path to the local XLSX file
xlsx_path = 'Faal.xlsx'  

# Read poems and definitions from the local XLSX file
poems = read_poems_from_xlsx(xlsx_path)

def start(update: Update, _: CallbackContext) -> None:
    """Start the bot and get a welcome message"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\! Send /fal to get a random Hafez poem\.',
        reply_markup=ForceReply(selective=True),
    )

def fal(update: Update, _: CallbackContext) -> None:
    """Get a random Hafez poem"""
    poem, definition = random.choice(poems)
    response = f"Poem:\n{poem}\n\nMeaning:\n{definition}"
    update.message.reply_text(response)

def text_message(update: Update, context: CallbackContext) -> None:
    # Check if the message text is '/fal'
    if update.message.text.lower() == '/fal':
        fal(update, context)

def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    # Set bot commands for suggestions
    commands = [
        BotCommand("start", "Start the bot and get a welcome message"),
        BotCommand("fal", "Get a random Hafez poem")
    ]
    updater.bot.set_my_commands(commands)

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("fal", fal))

    # Add MessageHandler for text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
