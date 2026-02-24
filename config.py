import os

bot_token = os.environ.get('SUPPORT_BOT_TOKEN', '')
supergroup_id = os.environ.get('SUPERGROUP_ID', '')
database_name = os.environ.get('DB_NAME', 'users.db')
log_level = os.environ.get('LOG_LEVEL', 'INFO')
