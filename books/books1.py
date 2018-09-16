import csv

def scanner(name) :
    with open(name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    csv = sys.argv[1]
    scanner(csv)
