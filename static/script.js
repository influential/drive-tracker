const deleteDrive = (event) => {
    // Grab values
    let drive = event.data.selected;

    console.log(drive);
    console.log("DELETING:");
    console.log('ticket: ' + drive[0]['ticketNumber']);
    console.log('serial: ' + drive[1]['serialNumber']);
    console.log('manufacturer: ' + drive[2]['manufacturer']);
    console.log('dateReceived: ' + drive[3]['dateReceieved']);
    console.log('dateToWipe: ' + drive[4]['dateToWipe']);
    console.log('id: ' + drive[5]['id']);


    // Build drive obeject
    const driveData = {
        "ticketNumber": drive[0]['ticketNumber'],
        "serialNumber": drive[1]['serialNumber'],
        "manufacturer": drive[2]['manufacturer'],
        "dateReceieved": drive[3]['dateReceieved'],
        "dateToWipe": drive[4]['dateToWipe'],
        "id": drive[5]['id'],
    }

    console.log(driveData);

    // Send values via AJAX POST request to Flask's /delete endpoint
    $.ajax({
        type: "POST",
        url: "/delete",
        data: driveData,
        // contentType: "application/json",
        dataType: 'text',
        error: function(request, status, errorThrown) {
            alert(errorThrown)
        },
        success: function(request) {
            // alert('Removed drive with serial ' + driveData['serialNumber']);
            // $("#driveTable").load( "home #driveTable" );
            window.location.reload();
        },
    }).then((res) => {
        console.log(res);
        return res;
    });
}

$(document).ready(function () {
    // Listen for a row to be clicked, grab the drive data
    $("#driveTable tr").click(function (e) {  
        let selectedDrive = [
            { ticketNumber: $(this)['0'].cells.ticketNumber.innerText },
            { serialNumber: $(this)['0'].cells.serialNumber.innerText }, 
            { manufacturer: $(this)['0'].cells.manufacturer.innerText },
            { dateReceieved: $(this)['0'].cells.dateReceieved.innerText },
            { dateToWipe: $(this)['0'].cells.dateToWipe.innerText },
            { id: $(this)['0'].cells.id.innerText },
        ]

        console.log(selectedDrive);
        console.log("SELECTED: ", selectedDrive[5]['id']);

        // When the confirm button is clicked, prepare data for Flask
        $("#deleteDriveConfirmBtn").click({selected: selectedDrive}, deleteDrive);
    });

    // By default, sort based on date to wipe in ascending order
    $("#driveTable").DataTable({
        order: [[5, 'asc']],
    })
});