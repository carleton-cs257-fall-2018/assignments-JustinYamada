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
        for item in authorsTemp:
            authorsTempData.append(item)
        # Need to compare lists of two authors

    return authorsTempData

def sort(array, direction, type):
    '''Sorts whatever it gets'''
    if type == "author" :
        cat = sorted(array, key=lambda x:x.split(" ")[-1])
    elif type == "book" :
        cat = sorted(array)

    if direction == "forwards" :
        return cat
    elif direction == "backwards" :
        return cat[::-1]
    else :
        sys.exit("Please use either \"forwards\" or \"backwards\" to specify order")

def search(array, key):
    '''Just here for temp testing purposes, ignore this'''
    for item in array:
        if item==key:
            return True
    return False

def main():

    if len(sys.argv)<2:
        sys.exit("What CSV file do you want me to use?")
    if len(sys.argv)<3:
        sys.exit("What direction do you want me to sort?")

    data = scanner(sys.argv[1])

    if sys.argv[2] == "books":
        print(sort(getBooks(data), sys.argv[3], "book"))
    if sys.argv[2] == "authors":
        print(sort(getAuthors(data), sys.argv[3], "author"))

if __name__=="__main__":
    main()
