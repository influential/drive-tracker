from Database import Database

db = Database()

drive = {
    'ticketNumber': '186230142',
    'serialNumber': 'Z90TS55555',
    'manufacturer': 'WD',
    'dateReceived': '2022-12-05',
    'dateToWipe': '	2023-04-04',
    'id': '184'
}

db.modify_drive(drive)
