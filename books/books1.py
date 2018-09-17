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
        authorsTempData.append(authorsTemp)
        # Need to compare lists of two authors

    return authors
    
def sort(array):
    '''Sorts whatever it gets'''
    return []

def search(array, key):
    '''Just here for temp testing purposes, ignore this'''
    for item in array:
        if item==key:
            return True
    return False


def main():

    if len(sys.argv)<2:
        sys.exit("What CSV file do you want me to use?")

    csv = sys.argv[1]
    data = scanner(csv)
    getBooks(data)
    getAuthors(data)


    # print(authorsTempData)
    #print("BOOKS ")
    #print(books)
    #print("AUTHORS ")
    #print(authors)
    scanner(csv)


if __name__=="__main__":
    main()
