initialize();

function initialize() {
    var maxElement = document.getElementById('max_button');
    if (maxElement) {
        element.onclick = onMostButtonClicked;
    }
    var minElement = document.getElementById('min_button');
    if (minElement) {
        element.onclick = onLeastButtonClicked;
    }
}


function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    console.log(baseURL);
    return baseURL;
}

function onMostButtonClick() {
    var url = getBaseURL() + '/frequency/max';
    // console.log(url);

    // Send the request to the Books API /authors/ endpoint
    console.log(fetch(url, {method: 'FREQUENCY'}))
    fetch(url, {method: 'FREQUENCY'})
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
        var tableBody = '<tr><th>' + zipcodeElement.value + '</th></tr>';
        for (var k = 0; k < crimesList.length; k++) {
            tableBody += '<td><a onclick="getCrime_code('
            + frequencyList[k][0]
            + ": code, " + frequencyList[k][1]
            + ",': occured " + frequencyList[k][2] + " times"
            + "')\">" 
            + '</a></td>';


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
          
function getCrime_code(buffer, police_code, buffer2) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getBaseURL() + '/frequency/max/' + police_code;

    fetch(url, {method: 'CRIMECODE'})

    .then((response) => response.json())

    .then(function(booksList) {
        var tableBody = '<tr><th>' + authorName + '</th></tr>';
        for (var k = 0; k < booksList.length; k++) {
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


}
