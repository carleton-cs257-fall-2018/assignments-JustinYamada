import csv
with open('books.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
