import csv
import sys
import re

def scanner(file):
    '''parses the csv file and returns an array of csv rows'''
    booksData = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            booksData.append(row)
    return booksData

def getBooks(data):
    '''Returns a array of book names, unsorted'''
    books = []
    for row in data:
        books.append(row[0])
    return books

def getAuthors(data):
    '''Returns a array of book authors, unsorted'''
    authors = []
    authorsTemp = []
    authorsTempData = []
    authorsFinal = []

    for row in data:
        authors.append(row[2])

    for author in authors:
        authorsTemp = re.split(' \(|\) and ',author)
        authorsTemp.pop()
        if len(authorsTemp) > 1:
            del authorsTemp[1]
            # does not account for three authors
        for item in authorsTemp:
            authorsTempData.append(item)
        # Need to compare lists of two authors

    return authorsTempData

def sort(array, type):
    '''Sorts array according to its type'''
    if len(sys.argv)<3:
        return array

    if type == "author" :
        cat = sorted(array, key=lambda x:x.split(" ")[-1])
    elif type == "book" :
        cat = sorted(array)

    if sys.argv[3] == "forward" :
        return cat
    elif sys.argv[3] == "reverse" :
        return cat[::-1]
    else :
        sys.exit("Please use either \"forward\" or \"reverse\" to specify order")

def printer(array) :
    '''Prints each element of the array NICLEY'''
    for item in array :
        print(item)

def main():

    if len(sys.argv)<2:
        sys.exit("What CSV file do you want me to use?")

    if sys.argv[2] == "books":
        books = getBooks(scanner(sys.argv[1]))
        sortedBooks = sort(books, "book")
        printer(sortedBooks)

    elif sys.argv[2] == "authors":
        authors = getAuthors(scanner(sys.argv[1]))
        sortedAuthors = sort(authors, "author")
        printer(sortedAuthors)

    else :
        sys.exit("Please speficiy either \"books\" or \"authours\"" )

if __name__=="__main__":
    main()
