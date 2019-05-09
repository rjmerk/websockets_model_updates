window.addEventListener('load', function() {
    const url = `ws://${ window.location.host }/ws/appointments/`;
    const socket = new WebSocket(url);
    socket.onclose = function(e) {
        console.error('Socket closed unexpectedly');
    };
    socket.onopen = function () {
        socket.send(JSON.stringify({
            "message": "jello"
        }));
    };

    socket.onmessage = function(e) {
        var message = JSON.parse(e.data);
        console.log("The server send us the following appointment: ");
        console.log(message['appointment_date']);
        console.log(message['description']);
    };

});
