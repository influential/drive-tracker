import sqlite3
import traceback
import sys


class Database:
    def __init__(self):
        self.db_locale = 'drives.db'
        self.connection = sqlite3.connect(self.db_locale)
        self.cursor = self.connection.cursor()

    def error(self, err):
        exc_type, exc_value, exc_tb = sys.exc_info()
        print('[-] SQLite Error: %s' % (' '.join(err.args)))
        print('[-] SQLite Traceback: ' + str(traceback.format_exception(exc_type, exc_value, exc_tb)))
        self.connection.close()
        return err.args

    def get_all(self):
        try:
            query = 'SELECT * FROM drive_details'
            self.cursor.execute(query)
            drive_data = self.cursor.fetchall()

            self.connection.commit()
            self.connection.close()

            print("[+] Retrieved all records from `drive_details`")
            return drive_data

        except sqlite3.Error as err:
            self.error(err)
            
    def populate_dummy(self, data):
        try:
            query = 'INSERT INTO drive_details (serial, ticket_number, manufacturer, date_received, date_to_wipe, date_received_unix, date_to_wipe_unix) VALUES (?, ?, ?, ?, ?, ?, ?)'
            # self.cursor.execute("""
            #     INSERT INTO drive_details (serial, ticket_number, manufacturer, date_received, date_to_wipe) VALUES
            #     ('HZ90S3', '199189230', 'Seagate', '2022-12-06', '2023-04-05'),
            #     ('Z90TS4', '186230142', 'WD', '2022-12-05', '2023-04-04'),
            #     ('03TS4X', 'N/A', 'Seagate', '2022-12-13', '2023-04-03')
            # """)

            self.cursor.executemany(query, data)

            self.connection.commit()
            self.connection.close()
            print("[+] Populated `drive_data` with dummy data")

        except sqlite3.Error as err:
            self.error(err)
            
    def drop_all(self):
        try:
            query = 'DELETE FROM drive_details'
            self.cursor.execute(query)
            self.connection.commit()
            self.connection.close()
            print("[+] Dropped all records from drive_details")

        except sqlite3.Error as err:
            self.error(err)

    def insert_drive(self, drive):
        try:
            query = 'INSERT INTO drive_details (ticket_number, serial, manufacturer, date_received, date_to_wipe, date_received_unix, date_to_wipe_unix) VALUES (?, ?, ?, ?, ?, ?, ?)'
            self.cursor.execute(query, drive)
            self.connection.commit()
            print(
                f"[+] Inserted {drive[1]} into `drive_details` with id={drive[0]}")
            self.connection.close()

        except sqlite3.Error as err:
            self.error(err)

    def delete_drive(self, drive_id):
        try:
            # Deletes based on serial number, should eventually switch to ID
            query = f"DELETE FROM drive_details WHERE id=?"
            self.cursor.execute(query, (drive_id,))
            self.connection.commit()
            print(
                f"[+] Removed drive with id `{drive_id}` from `drive_details`")
            self.connection.close()

        except sqlite3.Error as err:
            self.error(err)  

    def modify_drive(self, drive):
        try:
            print("INSIDE DATABASE MODIFY")

            query_data = {
                'serial': drive['serialNumber'],
                'ticketNumber': drive['ticketNumber'],
                'manufacturer': drive['manufacturer'],
                'dateReceived': drive['dateReceived'],
                'dateToWipe': drive['dateToWipe'],
                'id': drive['id']
            }

            query = f"UPDATE drive_details SET serial=:serial, ticket_number=:ticketNumber, manufacturer=:manufacturer, date_received=:dateReceived, date_to_wipe=:dateToWipe WHERE id=:id"

            self.cursor.execute(query, query_data)
            self.connection.commit()
            print(
                f"[+] Updated drive with id `{drive['id']}` from `drive_details`")
            self.connection.close()
            return

        except sqlite3.Error as err:
            self.error(err)
