#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import sys
import flask
import json





app = flask.Flask(__name__)

def scanner(file):
    '''parses the csv file and returns an array of csv rows'''
    Data = []
    with open(file, newline='') as f:
        # reader takes in the csv file
        reader = csv.reader(f)
        # copies all the information from the csv file into a new list
        for row in reader:
            Data.append(row)
    return Data

crimesFile = scanner(crime_filename)
crimeList = []
dictionary = {}
    for row in crimesFile:
        dictionary = {'id': int(row[0]), 'police_code': int(row[1]), 'type_place_broad': int(row[2]), 'type_place_specific': int(row[3]), 'crime_category': row[4], 'specific_crime': row[5], 'city': row[6]}
        crimeList.append(dictionary)

placeBroadFile = scanner(placeBroad_filename)
placeBroadList = []
dictionary = {}
    for row in crimesFile:
        dictionary = {'id': int(row[0]), 'type_place_broad': row[1]}
        placeBroadList.append(dictionary)

placeSpecificFile = scanner(placeSpecific_filename)
placeSpecificList = []
dictionary = {}
    for row in placeSpecificFile:
        dictionary = {'id': int(row[0]), 'type_place_specific': row[1]}
        placeSpecificList.append(dictionary)
            
@app.route('/crimes')
def hello():
    print("hello")
    return 'Hello, Welcome to the Crime database.'

@app.route('/crimes/',methods=['GET'])
    ast.literal_eval(request.args.get('zipcodes')),


@app.route('/crimes/frequency/max_frequency')
    return ''
@app.route('/crimes/frequency/min_frequency')
    return ''
@app.route('/actor/<last_name>')

def get_actor(last_name):
    ''' Returns the first matching actor, or an empty dictionary if there's no match. '''
    actor_dictionary = {}
    lower_last_name = last_name.lower()
    for actor in actors:
        if actor['last_name'].lower().startswith(lower_last_name):
            actor_dictionary = actor
            break
    return json.dumps(actor_dictionary)\





@app.route('/movies')
def get_movies():
    ''' Returns the list of movies that match GET parameters:
          start_year, int: reject any movie released earlier than this year
          end_year, int: reject any movie released later than this year
          genre: reject any movie whose genre does not match this genre exactly
        If a GET parameter is absent, then any movie is treated as though
        it meets the corresponding constraint. (That is, accept a movie unless
        it is explicitly rejected by a GET parameter.)
    '''
    movie_list = []
    genre = flask.request.args.get('genre')
    start_year = flask.request.args.get('start_year', default=0, type=int)
    end_year = flask.request.args.get('end_year', default=10000, type=int)
    for movie in movies:
        if genre is not None and genre != movie['genre']:
            continue
        if movie['year'] < start_year:
            continue
        if movie['year'] > end_year:
            continue
        movie_list.append(movie)

    return json.dumps(movie_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
