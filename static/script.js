const findTargetRow = () => {
    // let rows = document.getElementsByClassName("drive-row");
    $("#driveTable tr").click(function (e) {
        console.log("CLICK");
        let cells = e.currentTarget.cells;
        console.log(cells);   
        
    });

    // console.log(rows);
    // console.log(typeof(rows));


    // console.log(row_array);

    // rows_list.map(row => {
    //     row.addEventListener("click", (e) => {
    //         console.log(e.target);
    //     });
    // });
}

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

// const modifyDrive = (event) => {
//     console.log("MODIFY DRIVE CLICKED")
//     let drive = event.data.selected;

//     console.log(drive);
//     console.log("UPDATING:");
//     console.log('ticket: ' + drive[0]['ticketNumber']);
//     console.log('serial: ' + drive[1]['serialNumber']);
//     console.log('manufacturer: ' + drive[2]['manufacturer']);
//     console.log('dateReceived: ' + drive[3]['dateReceieved']);
//     console.log('dateToWipe: ' + drive[4]['dateToWipe']);

//     // Build drive obeject
//     const driveData = {
//         "ticketNumber": drive[0]['ticketNumber'],
//         "serialNumber": drive[1]['serialNumber'],
//         "manufacturer": drive[2]['manufacturer'],
//         "dateReceieved": drive[3]['dateReceieved'],
//         "dateToWipe": drive[4]['dateToWipe']
//     }

//     $.ajax({
//         type: "POST",
//         url: "/modify",
//         data: driveData,
//         // contentType: "application/json",
//         dataType: 'text',
//         error: function(request, status, errorThrown) {
//             alert(errorThrown)
//         },
//         success: function(request) {
//             console.log("UPDATE SUCCESS")
//             // alert('Removed drive with serial ' + driveData['serialNumber']);
//             // $("#driveTable").load( "home #driveTable" );
//             // window.location.reload();
//             // $("#ticketNumberForm").val(driveData['ticketNumber']);
//             // $("#serialNumberForm").val(driveData['serialNumber']);
//             // $("#manufacturerForm").val(driveData['manufacturer']);
//             // $("#dateReceievedForm").val(driveData['dateReceived']);
//             // $("#dateToWipeForm").val(driveData['dateToWipe']);

//             // $("#modifyDriveForm").load("home #modifyDriveForm");
//         },
//     }).then((res) => {
//         console.log(res);
//         return res;
//     });
// }

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

    $("#driveTable").DataTable({
        order: [[5, 'asc']],
    })
});