import sqlite3

db_locale = 'drives.db'

connection = sqlite3.connect(db_locale)
c = connection.cursor()

c.execute("""
CREATE TABLE drive_details 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_number TEXT,
    serial TEXT,
    manufacturer TEXT,
    date_received TEXT,
    date_to_wipe TEXT
)
""")

connection.commit()
connection.close()
