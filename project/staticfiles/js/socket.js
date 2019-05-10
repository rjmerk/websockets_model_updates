window.addEventListener('load', function() {
    const url = `ws://${ window.location.host }/ws/appointments/`;
    const socket = new WebSocket(url);
    socket.onclose = function(e) {
        console.error('Socket closed unexpectedly');
    };
    socket.onopen = function () {
        socket.send(JSON.stringify({
            "min_date": "2018-03-03",
        }));
    };

    socket.onmessage = function(e) {
        var message = JSON.parse(e.data);
        var row = createOrGetRow(message);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = message['appointment_date'];
        cell2.innerHTML = message['description'];
    };

    function createOrGetRow(message) {
        var table = document.getElementById("appointmentsTable");
        var row_id =  message['appointment_id'];
        var rows = document.querySelectorAll('#row-' + row_id);
        var row;
        if(rows.length !==0 ) {
            row = rows[0];
           row.innerHTML = "";
        } else {
            row = table.insertRow(-1);
            row.id = "row-" + row_id;
        }
        return row;
    }
});
