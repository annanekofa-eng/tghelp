# Telegram Support Bot (tghelp)

## Overview
A Telegram support bot that handles user messages, forum topics, and bidirectional communication through Telegram's Bot API.

## Architecture
- **Language**: Python 3.12
- **Framework**: python-telegram-bot v20.7
- **Database**: SQLite (local file `users.db`)
- **Entry Point**: `main.py`

## Project Structure
- `main.py` - Application entry point, sets up handlers and starts polling
- `config.py` - Configuration loader (reads from environment variables)
- `handlers.py` - Telegram bot command and message handlers
- `database.py` - SQLite database manager for user topics and support chats
- `requirements.txt` - Python dependencies

## Environment Variables
- `SUPPORT_BOT_TOKEN` (required) - Telegram Bot API token
- `SUPERGROUP_ID` (optional) - Telegram supergroup ID for support
- `DB_NAME` (optional, default: `users.db`) - SQLite database filename
- `LOG_LEVEL` (optional, default: `INFO`) - Logging level

## Running
The bot runs as a console workflow via `python main.py`. It uses long-polling to receive Telegram updates.
