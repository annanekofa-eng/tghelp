from telegram import Update
from telegram.ext import ContextTypes

from database import DatabaseManager

db = DatabaseManager()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text('Hello! Welcome to the bot. How can I assist you today?')


async def handle_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_id = str(update.effective_user.id)
    db.save_support_chat_record(user_id, user_message)
    await update.message.reply_text(f'You said: {user_message}')


async def handle_support_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    support_message = update.message.text
    await update.message.reply_text(f'Support: {support_message}')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update {update} caused error {context.error}')
