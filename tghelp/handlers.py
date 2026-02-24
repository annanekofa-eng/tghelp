from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! Welcome to the bot. How can I assist you today?')

def handle_user_message(update: Update, context: CallbackContext) -> None:
    """Handle user messages."""
    user_message = update.message.text
    update.message.reply_text(f'You said: {user_message}')

def handle_support_response(update: Update, context: CallbackContext) -> None:
    """Handle support responses."""
    support_message = update.message.text
    update.message.reply_text(f'Support: {support_message}')

def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    print(f'Update {update} caused error {context.error}')

def main() -> None:
    """Start the bot."""
    # Create the application and pass it your bot's token.
    application = ApplicationBuilder().token('YOUR_TOKEN').build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))

    # Message handlers
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_user_message))
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_support_response))

    # Error handler
    application.add_error_handler(error)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()