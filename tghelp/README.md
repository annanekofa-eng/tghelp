# Telegram Support Bot Documentation

## Overview
This document provides comprehensive details about the Telegram support bot for the project `tghelp`. 

## Installation Instructions
1. **Clone the Repository:**  
   Use the following command to clone the repository:
   ```bash
   git clone https://github.com/annanekofa-eng/tghelp.git
   ```  
2. **Install Dependencies:**  
   Navigate to the project directory and install the required packages:
   ```bash
   cd tghelp
   npm install
   ```  
3. **Set Up Environment Variables:**  
   Create a `.env` file in the root directory and specify your variables as follows:
   ```env
   TELEGRAM_BOT_TOKEN='YOUR_BOT_TOKEN'
   DATABASE_URL='YOUR_DATABASE_URL'
   ```  
4. **Run the Bot:**  
   Start the bot using:
   ```bash
   npm start
   ```

## Architecture
The bot is designed using the following components:
- **Bot API:** Interface with Telegram's Bot API.
- **Webhooks:** For receiving updates and messages.
- **Database:** To store user interactions and configurations.
- **Middleware:** To manage requests and responses.

## Database Schema
The database consists of the following tables:
1. **Users**:  
   - `user_id`: Unique identifier for the user
   - `username`: User's Telegram username
   - `created_at`: Timestamp of when the user was registered

2. **Messages**:  
   - `message_id`: Unique identifier for the message
   - `user_id`: Foreign key to the Users table
   - `content`: The content of the message
   - `timestamp`: The time the message was sent

3. **Settings**:  
   - `setting_id`: Unique identifier for the setting
   - `user_id`: Foreign key to the Users table
   - `preference`: User-specific preferences for bot interactions

## Troubleshooting Guide
- **Bot Not Responding:**  
  - Ensure the bot token is correct in the `.env` file.
  - Check if the bot is running and properly connected to the internet.

- **Database Connection Issues:**  
  - Verify that the `DATABASE_URL` is set correctly in the `.env` file and that the database service is up and running.

- **Unhandled Exceptions:**  
  - Check the logs for any unhandled exceptions and make sure to provide error handling in your code.