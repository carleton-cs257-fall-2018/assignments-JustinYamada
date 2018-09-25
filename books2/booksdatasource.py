#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''
def scanner(file):
    '''parses the csv file and returns an array of csv rows'''
    Data = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
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

        self.booksFile = scanner(books_filename)
        self.authorsFile = scanner(authors_filename)
        self.linkFile = scanner(books_authors_link_filename)
        self.authors = []
        self.books = []
        self.bookLink =[]
        self.authorLink = []

        dictionary = {}
        for row in self.booksFile:
            dictionary = {'id': row[0], 'title': row[1], 'publication_year': row[3]}
            self.books.append(dictionary)

        dictionary = {}
        for row in self.authorsFile:
            dictionary = {'id': row[0], 'last_name': row[1], 'first_name': row[2],
            'birth_year': row[3], 'death_year': row[4]}
            self.authors.append(dictionary)
        i = 0
        for row in self.linkFile:
            if i == row[0]:
                self.bookLink.append([row[1]])
                i++
            else:
                self.bookLink[row[0]].append(row[1])
            self.authorLink.append("null")

        for row in self.linkFile:
            if self.authorLink[row[1]] != "null":
                self.authorLink[row[1]] = [row[0]]
            else:
<<<<<<< HEAD
                self.authorLink[row[1]].append(row[0])
        
=======
                self.authorLink[row[1]] = self.authorLink[row[1]] + ", " + row[0]

>>>>>>> b80cde402c8caa38e330256cd6e2564a90caaa1c
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
        pass

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''

        '''A book is represented as a dictionary with the keys 'id', 'title',
        and 'publication_year'. For example, "Pride and Prejudice"
        (assuming an ID of 132) would look like this:

            {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

        '''

        booksCopy = self.books[book_id].copy()

        id = booksCopy.pop('book_id')
        title = booksCopy.pop('title')
        pubY = booksCopy.pop('publication_year')

        return {'id': id, 'title': title, 'publication_year': pubY}

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
        return []

    def list_by_author_id(author_id)

        booksReturn = []
        for bookId in self.authorLink[author_id]:
            booksReturn.append(self.books[bookId])
        
        return booksReturn
    
    def list_by_year(list, start_year, end_year):
        newList = []
        
        for x in list:
            if (x.get('start_year') >= start_year or start_year == None) && (x.get('end_year') <= end_year or end_year == None):
                newList = list[i].add
        return newList

    def sort_by(list, string, number):
        return []

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


        authorsCopy = self.authors[author_id].copy()

        id = authorsCopy.pop('book_id')
        last_name = authorsCopy.pop('last_name')
        first_name = authorsCopy.pop('first_name')
        birth_year = authorsCopy.pop('birth_year')
        death_year = authorsCopy.pop('death_year')

        return {'id': id, 'last_name': last_name, 'first_name': first_name, 'birth_year': birth_year, 'death_year': death_year}

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
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        return []


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.books(book_id=book_id)
