import csv
import sys
import re

def scanner(name):
    '''parses the csv file and returns an array of csv rows'''

    booksData = []
    with open(name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            booksData.append(row)
    return booksData

def getBooks(data):
    '''Returns a array of book names, unsorted'''
    return []
def getAuthors(data):
    '''Returns a array of book authors, unsorted'''
    return []
def sort(array):
    '''Sorts whatever it gets'''
    return []


def main():

    if len(sys.argv)<2:
        sys.exit("What CSV file do you want me to use?")

    csv = sys.argv[1]
    booksData = scanner(csv)
    books = []
    authors = []
    authorsTemp = []
    authorsTempData = []
    authorsFinal = []

    for bookList in booksData:
        books.append(bookList[0])
        authors.append(bookList[2])

    for author in authors:
        authorsTemp = re.split(' \(|\) and ',author)
        authorsTemp.pop()
        if len(authorsTemp) > 1:
            del authorsTemp[1]
            # does not account for three authors
        authorsTempData.append(authorsTemp)
        # Need to compare lists of two authors

    # print(authorsTempData)
    #print("BOOKS ")
    #print(books)
    #print("AUTHORS ")
    #print(authors)
    scanner(csv)


if __name__=="__main__":
    main()
