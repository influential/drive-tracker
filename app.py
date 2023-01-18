from flask import Flask, render_template, request, jsonify, redirect
from datetime import datetime, timedelta
from Database import Database

app = Flask(__name__)

# Home page that displays the main drive table
@app.route('/')
@app.route('/home')
def home_page():
    db = Database()
    drive_data = db.get_all()

    new_date = datetime.now() + timedelta(days=120)
    new_wipe_date = f'{new_date.month}/{new_date.day}/{new_date.year}'
    current_date = datetime.now()

    return render_template('home.html', drive_data=drive_data, date_120_from_now=new_wipe_date, current_date=current_date, new_wipe_date_raw=new_date)

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
