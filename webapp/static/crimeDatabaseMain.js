initialize();

function initialize() {
    console.log('HelloMy NAme');
    var element = document.getElementById('crimes_button');
    console.log('HelloMy NAme2');
    if (element) {
        console.log('HelloMy NAme3');
        element.onclick = onCrimesButtonClicked;
        console.log('HelloMy NAme4');
    }
}


function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    console.log(baseURL);
    return baseURL;
}

function onCrimesButtonClicked() {
    console.log('HelloMy NAme');

    var url = getBaseURL() + '/crimes';
    console.log(url);

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

            tableBody += '<td>' + crimesList[k]['id'] + '</td>';
            tableBody += '<td>' + crimesList[k]['police_code'] + '</td>';
            tableBody += '<td>' + crimesList[k]['zipcode'] + '</td>';
            tableBody += '<td>' + crimesList[k]['type_place_broad'] + '</td>';
            tableBody += '<td>' + crimesList[k]['type_place_specific'] + '</td>';
            tableBody += '<td>' + crimesList[k]['crime_category'] + '</td>';
            tableBody += '<td>' + crimesList[k]['specific_crime'] + '</td>';
            tableBody += '<td>' + crimesList[k]['city'] + '</td>';


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
