initialize();

function initialize() {
    var element = document.getElementById('crimes_button');
    if (element) {
        element.onclick = onCrimesButtonClicked;
    }
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}


function onCrimesButtonClicked() {
    var url = getBaseURL();

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(crimesList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < crimesList.length; k++) {
            tableBody += '<tr>';

            tableBody += '<td><a onclick="getCrimes(' + crimesList[k]['id'] + ",'"
                            + crimesList[k]['police_code'] + ' ' + crimesList[k]['zipCode'] + "')\">"
                            + crimesList[k]['type_place_broad'] + ', '
                            + crimesList[k]['first_name'] + '</a></td>';

            tableBody += '<td>' + authorsList[k]['birth_year'] + '-';
            if (crimesList[k]['death_year'] != 0) {
                tableBody += authorsList[k]['death_year'];
            }
            tableBody += '</td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}



// Taken from https://stackoverflow.com/questions/16779244/hide-show-advanced-option-using-javascript
$(document).ready(function () {
    $('#advancedOptions').hide();
    $('.advanced').click(function() {
        if ($('#advancedOptions').is(':hidden')) {
             $('#advancedOptions').slideDown();
        } else {
             $('#advancedOptions').slideUp();
        }
    });
});



$(document).ready(funciton()) {
  $.ajax
}
