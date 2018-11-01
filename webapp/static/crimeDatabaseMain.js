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

    if (zipcodeElement) {
      url += '?zipcode=' + zipcodeElement.value;
    }

    var zipcodeElement2
    console.log(document.getElementById('zipcode2').value)
    if(document.getElementById('zipcode2').value != '') {
      zipcodeElement2 = document.getElementById('zipcode2');
      url += '&zipcode2=' + zipcodeElement2.value;
    }
    else {
      url += '&zipcode2=' + '99999';
    }

    var zipcodeElement3
    if(document.getElementById('zipcode3').value != '') {
      zipcodeElement2 = document.getElementById('zipcode3');
      url += '&zipcode3=' + zipcodeElement3.value;
    }

    else {
      url += '&zipcode3=' + '99999';
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
            if (crimesList[k][2] == zipcodeElement.value && run) {
                tableBody += '<td>' + 'Zipcode 1 is: ' + zipcodeElement.value + '</td>';
                run = false;
            }

            if (document.getElementById('zipcode2').value != '' && crimesList[k][2] == zipcodeElement2.value && run2) {
                tableBody += '<td>' + 'Zipcode 2 is: ' + zipcodeElement2.value + '</td>';
                run2 = false;
            }
            if (document.getElementById('zipcode3').value != '' && crimesList[k][2] == zipcodeElement3.value && run3) {
                tableBody += '<td>' + 'Zipcode 3 is: ' + zipcodeElement3.value + '</td>';
                run3 = false;
            }
            tableBody += '<tr>';
            tableBody += '<td>' + crimesList[k][0] + '</td>';
            tableBody += '<td>' + crimesList[k][1] + '</td>';
            tableBody += '<td>' + crimesList[k][2] + '</td>';
                if (crimesList[k][3]==0)
                    tableBody += '<td>' + 'Residence' + '</td>';
                if (crimesList[k][3]==1)
                    tableBody += '<td>' + 'Retail' + '</td>';
                if (crimesList[k][3]==2)
                    tableBody += '<td>' + 'Convenience Store' + '</td>';
                if (crimesList[k][3]==3)
                    tableBody += '<td>' + 'Parking Lot' + '</td>';
                if (crimesList[k][3]==4)
                    tableBody += '<td>' + 'Street' + '</td>';
                if (crimesList[k][3]==5)
                    tableBody += '<td>' + 'Parking Garage' + '</td>';
                if (crimesList[k][3]==6)
                    tableBody += '<td>' + 'Park' + '</td>';
                if (crimesList[k][3]==7)
                    tableBody += '<td>' + 'Government Building' + '</td>';
                if (crimesList[k][3]==8)
                    tableBody += '<td>' + 'School/College' + '</td>';
                if (crimesList[k][3]==9)
                    tableBody += '<td>' + 'Other/Unknown' + '</td>';
                if (crimesList[k][3]==10)
                    tableBody += '<td>' + 'Hospital/Emergency Care Center' + '</td>';
                if (crimesList[k][3]==11)
                    tableBody += '<td>' + 'Jail/Prison' + '</td>';
                if (crimesList[k][3]==12)
                    tableBody += '<td>' + 'Air/Bus/Train/Metro Terminal' + '</td>';
                if (crimesList[k][3]==13)
                    tableBody += '<td>' + 'Hotel/Motel/Etc.' + '</td>';
                if (crimesList[k][3]==14)
                    tableBody += '<td>' + 'Lake/Waterway' + '</td>';
                if (crimesList[k][3]==15)
                    tableBody += '<td>' + 'Grocery/Supermaket' + '</td>';
                if (crimesList[k][3]==16)
                    tableBody += '<td>' + 'Liquor Store' + '</td>';
                if (crimesList[k][3]==17)
                    tableBody += '<td>' + 'Bar/Night Club' + '</td>';
                if (crimesList[k][3]==18)
                    tableBody += '<td>' + 'Bank' + '</td>';
                if (crimesList[k][3]==19)
                    tableBody += '<td>' + 'Resturant' + '</td>';
                if (crimesList[k][3]==20)
                    tableBody += '<td>' + 'Gas Station' + '</td>';
                if (crimesList[k][3]==21)
                    tableBody += '<td>' + 'Auto Repair' + '</td>';
                if (crimesList[k][3]==22)
                    tableBody += '<td>' + 'Theater' + '</td>';
                if (crimesList[k][3]==23)
                    tableBody += '<td>' + 'Construction Site' + '</td>';
                if (crimesList[k][3]==24)
                    tableBody += '<td>' + 'Wooded Area' + '</td>';
                if (crimesList[k][3]==25)
                    tableBody += '<td>' + 'Recreation Center' + '</td>';
                if (crimesList[k][3]==26)
                    tableBody += '<td>' + 'Commercial' + '</td>';
                if (crimesList[k][3]==27)
                    tableBody += '<td>' + 'Bank/S&L/Credit Union' + '</td>';
                if (crimesList[k][3]==28)
                    tableBody += '<td>' + 'Doctor/Dentist/Vet Office' + '</td>';
                if (crimesList[k][3]==29)
                    tableBody += '<td>' + 'Laundromat' + '</td>';
                if (crimesList[k][3]==30)
                    tableBody += '<td>' + 'Auto Dealership' + '</td>';
                if (crimesList[k][3]==31)
                    tableBody += '<td>' + 'Pool' + '</td>';
                if (crimesList[k][3]==32)
                    tableBody += '<td>' + 'Pawn Shop' + '</td>';
                if (crimesList[k][3]==33)
                    tableBody += '<td>' + 'Field/Open Space' + '</td>';
                if (crimesList[k][3]==34)
                    tableBody += '<td>' + 'Check Cashing Est.' + '</td>';
                if (crimesList[k][3]==35)
                    tableBody += '<td>' + 'Rental Storage Facility' + '</td>';
                if (crimesList[k][3]==36)
                    tableBody += '<td>' + 'Library' + '</td>';
                if (crimesList[k][3]==37)
                    tableBody += '<td>' + 'Pedestrian Tunnel' + '</td>';
                if (crimesList[k][3]==38)
                    tableBody += '<td>' + 'Church/Synagogue/Temple' + '</td>';
                if (crimesList[k][3]==39)
                    tableBody += '<td>' + 'Golf Course' + '</td>';
                if (crimesList[k][3]==40)
                    tableBody += '<td>' + 'Nursery' + '</td>';





                if (crimesList[k][4]==0)
                    tableBody += '<td>' + 'Apartment/Condo' + '</td>';
                if (crimesList[k][4]==1)
                    tableBody += '<td>' + 'Other' + '</td>';
                if (crimesList[k][4]==2)
                    tableBody += '<td>' + 'Drug Store/Pharmacy' + '</td>';
                if (crimesList[k][4]==3)
                    tableBody += '<td>' + 'County' + '</td>';
                if (crimesList[k][4]==4)
                    tableBody += '<td>' + 'Commercial' + '</td>';
                if (crimesList[k][4]==5)
                    tableBody += '<td>' + 'In vehicle' + '</td>';
                if (crimesList[k][4]==6)
                    tableBody += '<td>' + 'Residential' + '</td>';
                if (crimesList[k][4]==7)
                    tableBody += '<td>' + 'Single Family' + '</td>';
                if (crimesList[k][4]==8)
                    tableBody += '<td>' + 'Department/Discount Store' + '</td>';
                if (crimesList[k][4]==9)
                    tableBody += '<td>' + 'Bus Stop' + '</td>';
                if (crimesList[k][4]==10)
                    tableBody += '<td>' + 'Mall' + '</td>';
                if (crimesList[k][4]==11)
                    tableBody += '<td>' + 'Park & Ride' + '</td>';
                if (crimesList[k][4]==12)
                    tableBody += '<td>' + 'Yard' + '</td>';
                if (crimesList[k][4]==13)
                    tableBody += '<td>' + 'Townhouse/Duplex' + '</td>';
                if (crimesList[k][4]==14)
                    tableBody += '<td>' + 'Alley' + '</td>';
                if (crimesList[k][4]==15)
                    tableBody += '<td>' + 'Driveway' + '</td>';
                if (crimesList[k][4]==16)
                    tableBody += '<td>' + 'Clothing' + '</td>';
                if (crimesList[k][4]==17)
                    tableBody += '<td>' + 'School' + '</td>';
                if (crimesList[k][4]==18)
                    tableBody += '<td>' + 'Beer & Wine' + '</td>';
                if (crimesList[k][4]==19)
                    tableBody += '<td>' + 'Sporting Goods' + '</td>';
                if (crimesList[k][4]==20)
                    tableBody += '<td>' + 'ATM' + '</td>';
                if (crimesList[k][4]==21)
                    tableBody += '<td>' + 'Hardware' + '</td>';
                if (crimesList[k][4]==22)
                    tableBody += '<td>' + 'Rec Center' + '</td>';
                if (crimesList[k][4]==23)
                    tableBody += '<td>' + 'Carport' + '</td>';
                if (crimesList[k][4]==24)
                    tableBody += '<td>' + 'Nursing Home' + '</td>';
                if (crimesList[k][4]==25)
                    tableBody += '<td>' + 'Office Building' + '</td>';
                if (crimesList[k][4]==26)
                    tableBody += '<td>' + 'Shed' + '</td>';
                if (crimesList[k][4]==27)
                    tableBody += '<td>' + 'Metro' + '</td>';
                if (crimesList[k][4]==28)
                    tableBody += '<td>' + 'Video Store' + '</td>';
                if (crimesList[k][4]==29)
                    tableBody += '<td>' + 'Garage' + '</td>';
                if (crimesList[k][4]==30)
                    tableBody += '<td>' + 'Apt Ofc/Storage' + '</td>';
                if (crimesList[k][4]==31)
                    tableBody += '<td>' + 'Appliances/Electronics' + '</td>';
                if (crimesList[k][4]==32)
                    tableBody += '<td>' + 'Salon/Spa' + '</td>';
                if (crimesList[k][4]==33)
                    tableBody += '<td>' + 'Industrial park' + '</td>';
                if (crimesList[k][4]==34)
                    tableBody += '<td>' + 'Jewelry' + '</td>';
                if (crimesList[k][4]==35)
                    tableBody += '<td>' + 'Church' + '</td>';
                if (crimesList[k][4]==36)
                    tableBody += '<td>' + 'Beauty/Barber Shop' + '</td>';
                if (crimesList[k][4]==37)
                    tableBody += '<td>' + 'Mobile Home' + '</td>';
                if (crimesList[k][4]==38)
                    tableBody += '<td>' + 'Dry Cleaner' + '</td>';
                if (crimesList[k][4]==39)
                    tableBody += '<td>' + 'NULL' + '</td>';
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
