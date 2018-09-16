import csv
import os
import sys
import re

def scanner(name) :
    booksData = []
    with open(name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            booksData.append(row)
    return booksData

def main():
    csv = sys.argv[1]
<<<<<<< HEAD
    booksData = scanner(csv)
    #print(booksData)
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

    print(authorsTempData)
    
    #print("BOOKS ")
    #print(books)
    #print("AUTHORS ")
    #print(authors)
=======
    scanner(csv)


>>>>>>> 6ff06368bd4805f01986cee8a7fda8fce86e571e
main()
