#!/usr/bin/env python3
'''
    books_and_authors_converter.py
    Jeff Ondich, 24 April 2017
    Updated 20 April 2018
    Modified by Justin Hahn and Justin Yamada

    Sample code illustrating a simple conversion of the
    books & authors dataset represented as in books_and_authors.csv,
    into the books, authors, and books_authors tables (in
    CSV form).

    This is trickier than my json_to_tables.py example,
    because in the books.csv file, the authors are implicit
    in the list of books rather than being separated out
    into their own data structure as they are in the
    books_and_authors.json file.
'''
import sys
import re
import csv

def load_from_crime_csv_file(csv_file_name):

    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    crimes = []
    type_place_broad = []
    type_place_specific = []
    FirstRowSkip = True
    for row in reader:
        if FirstRowSkip == True:
            FirstRowSkip = False
            continue
        #assert len(row) == 26

        type_place = re.split(' - | -', row[15])
        if  type_place[0] not in type_place_broad:
            type_place_broad.append(type_place[0])

        if len(type_place) == 2 and type_place[1] not in type_place_specific:
            type_place_specific.append(type_place[1])

        if len(type_place) == 2:
            crime = {'id': row[0], 'police_code': row[1], 'zipCode': row[13],
                     'type_place_broad': type_place_broad.index(type_place[0]),
                     'type_place_specific': type_place_specific.index(type_place[1]),
                     'crime_category': row[7], 'specific_crime': row[8], 'city': row[11]}
        else:
            crime = {'id': row[0], 'police_code': row[1], 'zipCode': row[13],
                     'type_place_broad': type_place_broad.index(type_place[0]),
                     'type_place_specific': 'NULL',
                     'crime_category': row[7], 'specific_crime': row[8], 'city': row[11]}
        crimes.append(crime)

    csv_file.close()
    return (crimes, type_place_broad, type_place_specific)

def save_crimes_table(crimes, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for crimes in crimes:
        crimes_row = [crimes['id'], crimes['police_code'], crimes['zipCode'], crimes['type_place_broad'],crimes['type_place_specific'],
        crimes['crime_category'], crimes['specific_crime'], crimes['city']]
        writer.writerow(crimes_row)
    output_file.close()

def save_type_place_table(type_place, csv_file_name):
    ''' Save the types of places in CSV form, with each row containing
        (id, police code, zip code, type place broad, death year), where
        death year can be NULL. '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for place in type_place:
        row = [type_place.index(place), place]
        writer.writerow(row)
    output_file.close()

if __name__ == '__main__':
    crimes, type_place_broad, type_place_specific = load_from_crime_csv_file('Crime.csv')

    save_crimes_table(crimes, 'crimes.csv')
    save_type_place_table(type_place_broad, 'type_place_broad.csv')
    save_type_place_table(type_place_specific, 'type_place_specific.csv')
