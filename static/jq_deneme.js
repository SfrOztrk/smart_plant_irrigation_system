// GET request to server to retrieve water pump state.
function getStatus() {
    $.get("/status", function(serverResponse) {          
    console.log(serverResponse)
    // updateControls(serverResponse)                                   
    });
}


// POST Request to server to turn off the water pump manually.
function postPumpOff() {
    $.post("/pump/OFF", function(serverResponse) {
        console.log(serverResponse);
        // updateControls(serverResponse);
    });
}

// POST Request to server to turn on the water pump manually.
function postPumpOn() {
    $.post("/pump/ON", function(serverResponse) {
        console.log(serverResponse);
        // updateControls(serverResponse);
    });
}


// POST Request to server to set water pump state automatically.
function postAutoMode(payload) {
    $.post("/auto", payload, function(serverResponse) {
        console.log(serverResponse);
        // updateControls(serverResponse);
    });
}


// function updateControls(data) {
//     pump_status = data.pump;
//     if (pump_status == "OFF") {
//         $("input[type=checkbox].off-on").prop("checked", false)
//     }
//     else {
//         $("input[type=checkbox].off-on").prop("checked", true)
//     }
//     $("#pumpState").html(pump_status);
// }


$(document).ready(function() {
    // event listener for off-on button
    $("input[type=checkbox].off-on").click(function() {   // if click off-on checkbox

        $("input[type=checkbox].auto").prop("checked", false)   // disable the auto mode

        if ($(this).prop("checked") == true) {    // if off-on checkbox is true
            postPumpOn();
        }
        else {
            postPumpOff();
        }
    });

    // event listener for auto button
    $("input[type=checkbox].auto").click(function() {   

        if ($(this).prop("checked") == true) {
         
        } 
        else {
       
        }

    });

    // Initialise slider value form state on server.
    getPumpState() 
});