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

    var url = getBaseURL() + '/crimes';
    var zipcodeElement = document.getElementById('zipcode');
    var zipcodeElement2 = document.getElementById('zipcode2');
    var zipcodeElement3 = document.getElementById('zipcode3');

    if (zipcodeElement) {
      url += '?zipcode=' + zipcodeElement.value;
    }
    
    if (zipcodeElement2) {
      url += '&zipcode2=' + zipcodeElement2.value;
    }
    else {
      url += '?zipcode2=' + '99999';
    }
    
    if (zipcodeElement3) {
      url += '&zipcode3=' + zipcodeElement3.value;
    }
    else {
      url += '?zipcode3=' + '99999';
    }

    for(k=1; k < 41; k++) {
      console.log('place'+k);

      var place = document.getElementById('place'+k);
      if (document.getElementById('place'+k).checked) {
        url += '&'+place.name+'='+place.value;
      }
    }


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
        run = true;
        run2 = true;
        run3 = true;
        for (var k = 0; k < crimesList.length; k++) {
            if (crimesList[k][2].equals(zipcodeElement.value) && run) {
                tableBody += '<p>' + zipcodeElement.value + '</p>';
                run = false;
            }
            if (crimesList[k][2].equals(zipcodeElement.value) && run2) {
                tableBody += '<p>' + zipcodeElement2.value + '</p>';
                run2 = false;
            }
            if (crimesList[k][2].equals(zipcodeElement.value) && run3) {
                tableBody += '<p>' + zipcodeElement3.value + '</p>';
                run3 = false;
            }
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

    // var canvas = document.getElementById('myCanvas');


    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}
