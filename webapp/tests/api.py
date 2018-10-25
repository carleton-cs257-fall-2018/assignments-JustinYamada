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


@app.route('/')
def hello():
    print("Please enter a zipcode")
    return 'Hello, Welcome to the Crime database.'

@app.route('/crimes/frequency/<word>')
def frequency_crimes(word):
    try:
        frequencyDataMax = run.getFrequency(word)
        return(json.dumps(frequencyDataMax))

    except Exception as e:
        print(e)
    return("The frequency csv does not exist")


@app.route('/crimes/', methods=['GET'])
def search_by_zipCode():
    try:

        crimeData = run.getCrimes(int(request.args.get('zipcode')))
        crimeData += run.getCrimes(int(request.args.get('zipcode2')))
        crimeData += run.getCrimes(int(request.args.get('zipcode3')))

        crimeSorted = []
        has_Been_Sorted = 0
        if request.args.get('Residence') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 0:
                    crimeSorted.append(crime)
        if request.args.get('Street') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 1:
                    crimeSorted.append(crime)
        if request.args.get('Retail') == 'true':
            has_Been_Sorted = 1
            for crime in crimeData:
                if int(crime[3]) == 2:
                    crimeSorted.append(crime)
        if has_Been_Sorted == 0:
            return(json.dumps(crimeData))

        return(json.dumps(crimeSorted))

    except Exception as e:
        print(e)
    return("Incorrect url has been entered")


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

    def getFrequency(self, word):
        try:
            cursor = self.connection.cursor()
            query ='''
            SELECT *
            FROM crimeFrequency
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
