'''
    api.py
    Justin Hahn, Justin Yamada 23 October 2018

    API that takes in URL inputs and returns
    crimes information dictionaries in response
    to the searches.
'''

import sys
from flask import request
import flask
import json
import config
import psycopg2
from config import password
from config import database
from config import user

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.after_request
def set_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/crimes/frequency/<word>')
def frequency_crimes(word):
    try:
        frequencyData = run.getFrequency(word)
        return(json.dumps(frequencyData))

    except Exception as e:
        print(e)
    return("The frequency csv does not exist")

@app.route('/crimes/frequency/max/<code>')
def return_crimes_by_crime_code_max(code):
    try:
        crime_code_crimes = run.getCrimeCode(int(code))
        return(json.dumps(crime_code_crimes))

    except Exception as e:
        print(e)
    return("The crime code max return function does not work")

@app.route('/crimes/frequency/min/<code>')
def return_crimes_by_crime_code_min(code):
    try:
        crime_code_crimes = run.getCrimeCode(int(code))
        return(json.dumps(crime_code_crimes))

    except Exception as e:
        print(e)
    return("The crime code min return function does not work")


@app.route('/crimes', methods=['GET'])
def search_by_zipCode():
    try:
        #request three zipcodes
        crimeData = run.getCrimes(int(request.args.get('zipcode')))
        crimeData += run.getCrimes(int(request.args.get('zipcode2')))
        crimeData += run.getCrimes(int(request.args.get('zipcode3')))

        # sorts through all possibilities of location options
        crimeSorted = []
        has_Been_Sorted = 0
        if request.args.get('Residence') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 0:
                    crimeSorted.append(crime)
        if request.args.get('Retail') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 1:
                    crimeSorted.append(crime)
        if request.args.get('Convenience_Store') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 2:
                    crimeSorted.append(crime)
        if request.args.get('Parking_Lot') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 3:
                    crimeSorted.append(crime)
        if request.args.get('Street') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 4:
                    crimeSorted.append(crime)
        if request.args.get('Parking_Garage') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 5:
                    crimeSorted.append(crime)
        if request.args.get('Park') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 6:
                    crimeSorted.append(crime)
        if request.args.get('Government_Building') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 7:
                    crimeSorted.append(crime)
        if request.args.get('School_College') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 8:
                    crimeSorted.append(crime)
        if request.args.get('Other_Unknown') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 9:
                    crimeSorted.append(crime)
        if request.args.get('Hospital_Emerygency_Care_Center') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 10:
                    crimeSorted.append(crime)
        if request.args.get('Jail_Prison') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 11:
                    crimeSorted.append(crime)
        if request.args.get('Air_Bus_Train_Metro_Terminal') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 12:
                    crimeSorted.append(crime)
        if request.args.get('Hotel_Motel_Etc.') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 13:
                    crimeSorted.append(crime)
        if request.args.get('Lake_Waterway') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 14:
                    crimeSorted.append(crime)
        if request.args.get('Grocery_Supermaket') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 15:
                    crimeSorted.append(crime)
        if request.args.get('Liquor_Store') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 16:
                    crimeSorted.append(crime)
        if request.args.get('Bar_Night_Club') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 17:
                    crimeSorted.append(crime)
        if request.args.get('Bank') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 18:
                    crimeSorted.append(crime)
        if request.args.get('Resturant') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 19:
                    crimeSorted.append(crime)
        if request.args.get('Gas_Station') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 20:
                    crimeSorted.append(crime)
        if request.args.get('Auto_Repair') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 21:
                    crimeSorted.append(crime)
        if request.args.get('Theater') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 22:
                    crimeSorted.append(crime)
        if request.args.get('Construction_Site') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 23:
                    crimeSorted.append(crime)
        if request.args.get('Wooded_Area') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 24:
                    crimeSorted.append(crime)
        if request.args.get('Recreation_Center') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 25:
                    crimeSorted.append(crime)
        if request.args.get('Commercial') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 26:
                    crimeSorted.append(crime)
        if request.args.get('Bank_S&L_Credit_Union') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 27:
                    crimeSorted.append(crime)
        if request.args.get('Doctor_Dentist_Vet_Office') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 28:
                    crimeSorted.append(crime)
        if request.args.get('Laundromat') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 29:
                    crimeSorted.append(crime)
        if request.args.get('Auto_Dealership') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 30:
                    crimeSorted.append(crime)
        if request.args.get('Pool') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 31:
                    crimeSorted.append(crime)
        if request.args.get('Pawn_Shop') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 32:
                    crimeSorted.append(crime)
        if request.args.get('Field_Open_Space') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 33:
                    crimeSorted.append(crime)
        if request.args.get('Check_Cashing_Est.') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 34:
                    crimeSorted.append(crime)
        if request.args.get('Rental_Storage_Facility') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 35:
                    crimeSorted.append(crime)
        if request.args.get('Library') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 36:
                    crimeSorted.append(crime)
        if request.args.get('Pedestrian_Tunnel') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 37:
                    crimeSorted.append(crime)
        if request.args.get('Church_Synagogue_Temple') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 38:
                    crimeSorted.append(crime)
        if request.args.get('Golf_Course') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 39:
                    crimeSorted.append(crime)
        if request.args.get('Nursery') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 40:
                    crimeSorted.append(crime)

        # if none of the locations are selected all results from the zipcodes returned
        if has_Been_Sorted == 0:
            return(json.dumps(crimeData))

        return(json.dumps(crimeSorted))

    except Exception as e:
        print(e)
    return("Incorrect url or location has been entered (Error, zipcode)")


class api:

    def getConnection(self):
        '''
        Returns a connection to the database described
        in the config module. Returns None if the
        connection attempt fails.
        '''

        try:
            self.connection = psycopg2.connect(database=config.database,
                                          user=config.user,
                                          password=config.password)
        except Exception as e:
            print(e, file=sys.stderr)
            exit()

    def get_select_query_results(connection, query, parameters=None):
        '''
        Executes the specified query with the specified tuple of
        parameters. Returns a cursor for the query results.
        Raises an exception if the query fails for any reason.
        '''
        cursor = connection.cursor()
        if parameters is not None:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        return cursor

    def getCrimes(self, zipcode):
        try:
            cursor = self.connection.cursor()
            query ='''
            SELECT *
            FROM crimes
            WHERE zipcode = {}
            '''.format(zipcode)

            cursor.execute(query)
            crimeData = []
            for row in cursor:
                crimeData.append(row)
            return crimeData

        except Exception as e:
            print(e)
            return None

    def getCrimeCode(self, code):
        try:
            cursor = self.connection.cursor()
            query ='''
            SELECT *
            FROM crimes
            WHERE police_code = {}
            '''.format(code)

            cursor.execute(query)
            crimeCodeData = []
            for row in cursor:
                crimeCodeData.append(row)
            return crimeCodeData

        except Exception as e:
            print(e)
            return ('The crime_code code or word is not working')

    def getFrequency(self, word):
        try:
            cursor = self.connection.cursor()
            query ='''
            SELECT *
            FROM crimefrequency
            ORDER BY frequency
            '''
            if word == 'max':
                query += 'DESC'
            if word == 'min':
                query += 'ASC'

            cursor.execute(query)
            frequencyData = []

            for row in cursor:
                frequencyData.append(row)

            return frequencyData

        except Exception as e:
            print(e)
            return ('The frequency code or word is not working')

    def shutdown(self):
        self.connection.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    run = api()
    run.getConnection()
    app.run(host=host, port=port, debug=True)
    run.shutdown()
