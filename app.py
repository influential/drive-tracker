from flask import Flask, render_template, request, jsonify, redirect
from datetime import datetime, timedelta
import time
from Database import Database

app = Flask(__name__)


def enum_dates(dates):
    result = {
        'ready_count': 0,
        'hold_count': 0,
    }
    todays_date = time.time()
    print("todays date:", float(todays_date))
    for date in dates:
        print("date:", float(date))
        if float(date) <= float(todays_date):
            result['ready_count'] += 1
        else:
            result['hold_count'] += 1
    return result



# Home page that displays the main drive table
@app.route('/')
@app.route('/home')
def home_page():
    data = {}
    db = Database()
    data['drive_data'] = db.get_all()
    dates = [d[7] for d in data['drive_data']]
    data['ready_stats'] = enum_dates(dates)
    data['new_date'] = datetime.now() + timedelta(days=120)
    data['new_wipe_date'] = f'{data["new_date"].month}/{data["new_date"].day}/{data["new_date"].year}'
    data['current_date'] = datetime.now()

    # print(data['new_date'])
    # print(data['ready_stats'])

    return render_template('home.html', data=data)


# Route for adding new drives
@app.route('/add', methods=['POST'])
def add_drive():
    db = Database()

    if request.method == 'POST':
        # Build new drive based on modal form input
        new_drive = (
            request.form['ticketNumber'],
            request.form['serialNumber'],
            request.form['manufacturer'],
            request.form['dateReceieved'],
            request.form['dateToWipe'],
            
            # ADD UNIX TIMES TO DB
            # request.form['dateReceieved'],
            # request.form['dateToWipe'],

        )
        db.insert_drive(new_drive)  # Insert the drive into DB
        return redirect('home')

# Route for removing drives based on serial
@app.route('/delete', methods=['POST'])
def delete_drive():
    db = Database()

    if request.method == 'POST':
        # Get drive data from selected row
        drive = request.form
        drive_id = drive['id']
        print("SERIAL FROM FRONTEND:", drive_id)

        # Remove drive based on selected serial
        db.delete_drive(drive_id)
        return redirect('home')


# Route for modifying drives based on serial
@app.route('/modify', methods=['POST'])
def modify_drive():
    db = Database()

    if request.method == 'POST':
        # Get drive data from modify form POST submission
        new_drive = request.form

        print("TARGET DRIVE FROM FRONTEND:")
        for x in new_drive:
            print(f"== {x}: {new_drive[x]}")

        # Modify drive based on selected serial
        db.modify_drive(new_drive)
        return redirect('home')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
