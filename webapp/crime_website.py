#!/usr/bin/env python3
'''
    books_api.py
    Jeff Ondich, 25 April 2016

    Simple Flask app used in the sample web app for
    CS 257, Spring 2016. This is the Flask app for the
    "books and authors" API and website. The API offers
    JSON access to the data, while the website (at
    route '/') offers end-user browsing of the data.
'''
import sys
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/crimes')
def get_main_page():
    ''' This is the only route intended for human users '''
    global api_port
    return flask.render_template('crimeDatabaseMain.html', api_port=api_port)

@app.route('/crimes/frequency/max')
def get_frequency_max_page():
    ''' This is the only route intended for human users '''
    global api_port
    return flask.render_template('frequencyMax.html', api_port=api_port)

@app.route('/crimes/frequency/min')
def get_frequency_min_page():
    ''' This is the only route intended for human users '''
    global api_port
    return flask.render_template('frequencyMin.html', api_port=api_port)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} host port api-port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    api_port = sys.argv[3]
    app.run(host=host, port=port)
