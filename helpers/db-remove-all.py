import sqlite3

db_locale = 'drives.db'

connection = sqlite3.connect(db_locale)
c = connection.cursor()

c.execute("""
DELETE FROM drive_details
""")

# drive_data = c.fetchall()

# c.rowcount()
print("[+] Dropped all records from drive_details")

connection.commit()
connection.close()
