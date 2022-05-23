// GET request to server to retrieve water pump state.
function getState() {
    $.get("/pump", function(serverResponse, status) {          
    console.log(serverResponse)
    updateControls(serverResponse)                                   
    });
}


// POST Request to server to set water pump state.
function postUpdate(payload) {
    $.posta("/pump", payload, function(serverResponse, status) {
        console.log(serverResponse);
        updateControls(serverResponse);
    });
}


function updateControls(data) {
    str = "";
    if (data.level == 1) {
        str = "Off"
        $("input[type=checkbox].off-on").prop("checked", false)
    }
    else {
        $("input[type=checkbox].off-on").prop("checked", true)
        str = "On"
    }
    $("#pumpState").html(str);
}

// Event listener for button value changes.
$(document).ready(function() {
    $("input[type=checkbox].off-on").click(function() {   

        $("input[type=checkbox].auto").prop("checked", false)  // disable the auto mode

        if ($(this).prop("checked") == true) {
            payload = { 
                "level": 0
            }    
        }
        else {
            payload = { 
                "level": 1
            }  
        }
        postUpdate(payload);
        }
    );

    $("input[type=checkbox].auto").click(function() {   

        if ($(this).prop("checked") == true) {
         
        } 
        else {
       
        }

    });

    // Initialise slider value form state on server.
    getState() 
});