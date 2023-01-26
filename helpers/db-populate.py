import string
import random
import time
from datetime import datetime, timedelta
from Database import Database


# Generates a date within the specified start and end range
# Adapted from: https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
def calc_date(start, end, time_format, prop):
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    p_time = start_time + prop * (end_time - start_time)
    return time.strftime(time_format, time.localtime(p_time))


def get_random_ticket(length=9):
    return ''.join(random.choice(string.digits) for i in range(length))


def get_random_serial(length=7):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length))


def get_random_manufacturer():
    options = ['Seagate', 'WD', 'Toshiba', 'Kingston', 'SanDisk']
    return random.choice(options)


def get_random_dates():
    start = "2022-1-1"
    end = "2023-12-31"
    prop = random.random()
    received = calc_date(start, end, '%Y-%m-%d', prop)
    to_wipe = datetime.strftime(datetime.strptime(
        received, '%Y-%m-%d') + timedelta(days=120), '%Y-%m-%d')

    received_unix, to_wipe_unix = get_dates_unix(received, to_wipe)
    return received, to_wipe, received_unix, to_wipe_unix


def get_dates_unix(received, to_wipe):
    received_unix = time.mktime(
        datetime.strptime(received, '%Y-%m-%d').timetuple())

    to_wipe_unix = time.mktime(
        datetime.strptime(to_wipe, '%Y-%m-%d').timetuple())

    return received_unix, to_wipe_unix


def build_dummy():
    serial = get_random_serial()
    ticketNumber = get_random_ticket()
    manufacturer = get_random_manufacturer()
    dateReceived, dateToWipe, dateReceivedUnix, dateToWipeUnix = get_random_dates()
    return (serial, ticketNumber, manufacturer, dateReceived, dateToWipe, dateReceivedUnix, dateToWipeUnix)


def generate_dummy_data():
    data = []
    for i in range(30):
        dummy = build_dummy()
        data.append(dummy)
    return data


data = generate_dummy_data()
db = Database()
db.populate_dummy(data)
