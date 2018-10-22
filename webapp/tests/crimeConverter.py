#!/usr/bin/env python3
'''
    books_and_authors_converter.py
    Jeff Ondich, 24 April 2017
    Updated 20 April 2018

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
    ''' Collect all the data from my sample books_and_authors.csv file,
        assembling it into a list of books, a dictionary of authors,
        and a list of book/author ID links. Rather than fully
        documenting the data structures built in this function and
        used in the later functions, I'm going to let you play around
        with it. I recommend just sticking some print statements
        in various places (or set some breakpoints if you use an IDE
        for Python, like PyCharm). You might find it interesting to
        figure out why I needed to use a dictionary for authors, but not
        for books.
    '''
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)
    
    crimes = []
    type_place_broad = []
    type_place_specific = []
    for row in reader:
        assert len(row) == 26
    
        type_place = row[15].split()
        if !(type_place[0] in type_place_broad):
            type_place_broad.append(type_place[0])
            
        if !(type_place[2] in type_place_specific):
            type_place_specific.append(type_place[2])
            
        crime = {'id': row[0], 'police_code': row[1], 'zipCode': row[13], 'type_place_broad': type_place_broad.index(type_place[0]), 'type_place_specific' : type_place_specific.index(type_place[2]),'crime_category' : row[7], 'specific_crime' : row[8], 'city' : row[11]}
        crimes.append(crime)

    csv_file.close()
    return (crimes, type_place_broad, type_place_specific)

def save_crimes_table(crimes, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for crimes in crimes:
        crimes_row = [crimes['id'], crimes['police_code'], crimes['zipCode'], crimes['type_place'],
         crimes['crime_category'], crimes['specific_crime'], crimes['city']]
        writer.writerow(crimes_row)
    output_file.close()

def save_authors_table(authors, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, last name, first name, birth year, death year), where
        death year can be NULL. '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for author in sorted(authors, key=authors.get):
        (last_name, first_name, birth_year, death_year) = author
        if death_year == '':
            death_year = 'NULL'
        author_id = authors[author]
        author_row = [author_id, last_name, first_name, birth_year, death_year]
        writer.writerow(author_row)
    output_file.close()

def save_linking_table(books_authors, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (book id, author id). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for book_author in books_authors:
        books_authors_row = [book_author['book_id'], book_author['author_id']]
        writer.writerow(books_authors_row)
    output_file.close()

if __name__ == '__main__':
    books, authors, books_authors = load_from_books_csv_file('books-original.csv')

    save_books_table(books, 'books.csv')
    save_authors_table(authors, 'authors.csv')
    save_linking_table(books_authors, 'books_authors.csv')
