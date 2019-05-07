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
        var data = JSON.parse(e.data);
        var message = data['message'];
        console.log("The server send us the following message: ");
        console.log(message);
    };

});
