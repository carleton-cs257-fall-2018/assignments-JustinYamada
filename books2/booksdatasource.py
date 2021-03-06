#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''

import csv
from operator import itemgetter

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


class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871


                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6

                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''

        self.booksFile = scanner(books_filename)
        self.authorsFile = scanner(authors_filename)
        self.linkFile = scanner(books_authors_link_filename)
        self.authorsList = []
        self.booksList = []
        self.bookLink =[]
        self.authorLink = []

        dictionary = {}
        for row in self.booksFile:
            dictionary = {'id': int(row[0]), 'title': row[1], 'publication_year': int(row[2])}
            self.booksList.append(dictionary)

        dictionary = {}
        for row in self.authorsFile:
            dictionary = {'id': int(row[0]), 'last_name': row[1], 'first_name': row[2],
            'birth_year': int(row[3]), 'death_year': int(row[4])}
            self.authorsList.append(dictionary)

        i = 0
        for row in self.linkFile:
            if i == int(row[0]):
                self.bookLink.append([int(row[1])])
                i += 1

            else:
                self.bookLink[int(row[0])].append(int(row[1]))
            self.authorLink.append("null")

        for row in self.linkFile:
            if self.authorLink[int(row[1])] == "null":
                self.authorLink[int(row[1])] = [int(row[0])]
            else:

                self.authorLink[int(row[1])].append(int(row[0]))

        pass

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''

        '''A book is represented as a dictionary with the keys 'id', 'title',
        and 'publication_year'. For example, "Pride and Prejudice"
        (assuming an ID of 132) would look like this:

            {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

        '''

        # returns the the specified book using the book_id
        return self.booksList[book_id].copy()

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            See the BooksDataSource comment for a description of how a book is represented.
        '''

        # creates new list to input the full book list into
        books_matching_criteria = self.booksList

        # questions if author_id is inputted and returns books that match value
        if author_id != None:
            books_matching_criteria = self.list_by_author_id(author_id)
        # questions if search_text is inputted and returns books that match value
        if search_text != None:
            books_matching_criteria = self.list_by_search_text(books_matching_criteria, search_text)
        # questions if start_year is inputted and returns books that match value
        if start_year != None or end_year != None:
            books_matching_criteria = self.list_by_year(books_matching_criteria, start_year, end_year)
        # sorts by year if the sort_by value is 'year'
        if sort_by == 'year':
            books_matching_criteria = self.sort_by_year(books_matching_criteria)
        # sorts by title if the sort value is anything else
        else:
            books_matching_criteria = self.sort_by_title(books_matching_criteria)

        # returns resulting book list sorted by terms
        return books_matching_criteria

    # author_id is inputted and books that contain the same author_id are appended into a list
    def list_by_author_id(self, author_id):

        booksReturn = []
        for bookId in self.authorLink[int(author_id)]:
            booksReturn.append(self.booksList[int(bookId)])

        return booksReturn

    # returns books that contain search text in title
    def list_by_search_text(self, bookList, string):
        newList = []

        for x in bookList:

            if (x['title'].upper()).find(string.upper()) > -1:
                newList.append(x)
        return newList

    # returns books that were published between start and/or end year
    def list_by_year(self, bookList, start_year, end_year):
        newList = []

        for x in bookList:
            if (x['publication_year'] >= start_year or start_year == None) and (x['publication_year'] <= end_year or end_year == None):
                newList.append(x)
        return newList

    # sorts the books titles alphabetically breaks ties by publication year
    def sort_by_title(self, bookList):
        bookList1 = sorted(bookList, key=lambda k: k['publication_year'])
        bookList2 = sorted(bookList1, key=lambda k: k['title'])
        return bookList2

    # sorts the books by publication year and then sorts the titles alphabetically during ties
    def sort_by_year(self, bookList):
        bookList1 = sorted(bookList, key=lambda k: k['title'])
        bookList2 = sorted(bookList1, key=lambda k: k['publication_year'])
        return bookList2


    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)
            An author is represented as a dictionary with the keys
            'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
            For example, Jane Austen would be represented like this
            (assuming her database-internal ID number is 72):

                {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
                 'birth_year': 1775, 'death_year': 1817}

            For a living author, the death_year is represented in the author's
            Python dictionary as None.

                {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
                 'birth_year': 1949, 'death_year': None} '''

        return self.authorsList[author_id].copy()

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):

        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive)
                last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        authorsReturn = self.authorsList

        # Checks to see which arguments are given and passes the list of authors
        # through each applicable function

        if book_id != None:
            authorsReturn = self.list_by_book_id(book_id)
        if search_text != None:
            authorsReturn = self.list_by_search_text_author(authorsReturn, search_text)
        if start_year != None or end_year != None:
            authorsReturn = self.list_by_year_author(authorsReturn, start_year, end_year)
        if sort_by == 'birth_year':
            authorsReturn = self.sort_by_birth_year(authorsReturn)
        else:
            authorsReturn = self.sort_by_else(authorsReturn)

        return authorsReturn

    # Returns a list of authors that have written a specific book given a book id
    def list_by_book_id(self, book_id):

        authorsReturn = []
        for authorId in self.bookLink[int(book_id)]:
            authorsReturn.append(self.authorsList[int(authorId)])

        return authorsReturn

    # Returns a list of authors with a string in their first or last name
    # given a list to search through and a string to look for in the author's names
    def list_by_search_text_author(self, authorsList, string):
        newList = []

        for x in authorsList:

            last = (x['last_name'].upper()).find(string.upper())
            first = (x['first_name'].upper()).find(string.upper())
            if last > -1 or first > -1:
                newList.append(x)
        return newList

    # Returns a list of authors that were alive during a time period given
    # a start year and end year and list of authors
    def list_by_year_author(self, authorsList, start_year, end_year):

        newList = []
        for x in authorsList:
            if (int((x['death_year']) >= int(start_year) or start_year == None) and (x['birth_year'] <= int(end_year) or end_year == None)):
                newList.append(x)
        return newList

    # Sorts a list of authors by birthyear then last name then first name
    def sort_by_birth_year(self, authorsList):

        authorsList1 = sorted(authorsList, key=lambda k: k['first_name'])
        authorsList2 = sorted(authorsList1, key=lambda k: k['last_name'])
        authorsList3 = sorted(authorsList2, key=lambda k: k['birth_year'])
        return authorsList3

    # Sorts a list of authors by last name then first name then birth year
    def sort_by_else(self, authorsList):

        authorsList1 = sorted(authorsList, key=lambda k: k['birth_year'])
        authorsList2 = sorted(authorsList1, key=lambda k: k['first_name'])
        authorsList3 = sorted(authorsList2, key=lambda k: k['last_name'])
        return authorsList3

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.authors(book_id=book_id)
