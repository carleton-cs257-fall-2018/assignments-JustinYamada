initialize();

function initialize() {
    

    var maxElement = document.getElementById('max_button');
    if (maxElement) {
        maxElement.onclick = onButtonClick("max");
    }

}


function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function onButtonClick(word) {
    var url = getBaseURL() + '/crimes/frequency/' + word;
    // console.log(url);

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})
    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).

    .then((response) => response.json())
    // .then(response => response.text())          // convert to plain text
    // console.log(response)
    // .then(text => console.log(text))

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(frequencyList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < frequencyList.length; k++) {

            tableBody += '<p><a onclick="getCrimeCode('
            + frequencyList[k][1]
            + ")\">"
            + frequencyList[k][0] + ': code '
            + frequencyList[k][1] + ': '
            + frequencyList[k][2] + ' occurences' +
            '</a></p>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('frequency_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }

      })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });

}


function getCrimeCode(police_code) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/crimes/frequency/max/' + police_code;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(crimesList) {
        var tableBody = '';
        for (var k = 0; k < crimesList.length; k++) {
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
        var resultsTableElement = document.getElementById('side_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}
