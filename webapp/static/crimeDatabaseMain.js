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
    console.log('HelloMy NAme6');
    var url = getBaseURL() + '/crimes';
    var zipcodeElement = document.getElementById('zipcode');
    if (zipcodeElement) {
      url += '?zipcode=' + zipcodeElement.value;
    }

    // console.log(url);

    // Send the request to the Books API /authors/ endpoint
    console.log(fetch(url, {method: 'GET'}))
    fetch(url, {method: 'get'})
    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).

    .then((response) => response.json())
    // .then(response => response.text())          // convert to plain text
    // console.log(response)
    // .then(text => console.log(text))

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(crimesList) {
        // Build the table body.
        var tableBody = '<tr><th>' + zipcodeElement.value + '</th></tr>';
        for (var k = 0; k < crimesList.length; k++) {
            console.log(crimesList[k] );
            tableBody += '<tr>';
            tableBody += '<td>' + crimesList[k][0] + '</td>';
            tableBody += '<td>' + crimesList[k][1] + '</td>';
            tableBody += '<td>' + crimesList[k][2] + '</td>';
            tableBody += '<td>' + crimesList[k][3] + '</td>';
            tableBody += '<td>' + crimesList[k][4] + '</td>';
            tableBody += '<td>' + crimesList[k][5] + '</td>';
            tableBody += '<td>' + crimesList[k][6] + '</td>';
            tableBody += '<td>' + crimesList[k][7] + '</td>';
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
