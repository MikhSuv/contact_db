import sqlite3


conn = sqlite3.connect('contacts.db')


cursor = conn.cursor()


cursor.execute('''
               CREATE TABLE IF NOT EXISTS contacts (
               id INTEGER PRIMARY KEY,
               first_name TEXT,
               last_name TEXT,
               phone_number TEXT,
               email TEXT
               )
               ''')
conn.close()

print("База данных 'contacts.db' успешно создана.")
