import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
SUPERGROUP_ID = -1001234567890  # Replace with your supergroup ID

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the support bot! Please describe your issue.')

# Message handler for user support requests
def support_request(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user = update.message.from_user
    logger.info(f"Received support request from {user.first_name}: {user_message}")
    
    # Forward the user's message to the supergroup
    context.bot.send_message(chat_id=SUPERGROUP_ID, text=f"New support request from {user.first_name} ({user.id}): {user_message}")

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it the bot token
    updater = Updater(TOKEN)

    # Register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, support_request))

    # Start the bot
    updater.start_polling()
    logger.info("Bot is polling...")
    updater.idle()

if __name__ == '__main__':
    main()