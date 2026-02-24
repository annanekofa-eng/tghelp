import sqlite3

class DatabaseManager:
    def __init__(self, db_name='users.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_topics (
                                id INTEGER PRIMARY KEY,
                                user_id TEXT NOT NULL,
                                topic TEXT NOT NULL
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS support_chats (
                                id INTEGER PRIMARY KEY,
                                user_id TEXT NOT NULL,
                                message TEXT NOT NULL,
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                            )''')
        self.connection.commit()

    def save_user_topic(self, user_id, topic):
        self.cursor.execute('INSERT INTO user_topics (user_id, topic) VALUES (?, ?)', (user_id, topic))
        self.connection.commit()

    def get_user_topics(self, user_id):
        self.cursor.execute('SELECT topic FROM user_topics WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def save_support_chat_record(self, user_id, message):
        self.cursor.execute('INSERT INTO support_chats (user_id, message) VALUES (?, ?)', (user_id, message))
        self.connection.commit()

    def get_support_chat_records(self, user_id):
        self.cursor.execute('SELECT message, timestamp FROM support_chats WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()