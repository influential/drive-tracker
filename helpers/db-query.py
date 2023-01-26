import sqlite3

db_locale = 'drives.db'

connection = sqlite3.connect(db_locale)
c = connection.cursor()

c.execute("""
SELECT * FROM drive_details
""")

drive_data = c.fetchall()

for d in drive_data:
    print(d)

connection.commit()
connection.close()
