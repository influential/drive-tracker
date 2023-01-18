# import sqlite3
# import sys
# import traceback
from Database import Database
# db_locale = 'drives.db'

# connection = sqlite3.connect(db_locale)
# c = connection.cursor()

# # c.execute("""
# # INSERT INTO drive_details (serial, ticket_number, manufacturer, date_received, date_to_wipe) VALUES
# # ('HZ90S3', '199189230', 'Seagate', '2022-12-6 08:38:00', '2023-4-5 08:38:00'),
# # ('Z90TS4', '186230142', 'WD', '2022-12-5 09:40:00', '2023-4-4 09:40:00'),
# # ('03TS4X', 'N/A', 'Seagate', '2022-12-3 10:40:00', '2023-4-3 09:40:00')
# # """)

# try:
#     c.execute("""
#         INSERT INTO drive_details () VALUES
#         ('HZ90S3', '199189230', 'Seagate', '2022-12-6 08:38:00', '2023-4-5 08:38:00'),
#         ('Z90TS4', '186230142', 'WD', '2022-12-5 09:40:00', '2023-4-4 09:40:00'),
#         ('03TS4X', 'N/A', 'Seagate', '2022-12-3 10:40:00', '2023-4-3 09:40:00')
#     """)

#     connection.commit()

# except sqlite3.Error as err:
#     exc_type, exc_value, exc_tb = sys.exc_info()

#     print('[-] SQLite Error: %s' % (' '.join(err.args)))
#     print('[-] SQLite Traceback: ' +
#           str(traceback.format_exception(exc_type, exc_value, exc_tb)))

# connection.commit()
# connection.close()

db = Database()
db.populate_dummy()
