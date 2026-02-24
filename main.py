import logging
import sys

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from config import bot_token, log_level
from handlers import start, handle_user_message, error

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, log_level, logging.INFO)
)
logger = logging.getLogger(__name__)


def main() -> None:
    if not bot_token:
        logger.error("SUPPORT_BOT_TOKEN environment variable is not set.")
        print("Error: SUPPORT_BOT_TOKEN is required. Please set it as a secret.")
        sys.exit(1)

    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_message))
    application.add_error_handler(error)

    logger.info("Bot started polling...")
    print("Bot is running and polling for updates...")
    application.run_polling()


if __name__ == '__main__':
    main()
