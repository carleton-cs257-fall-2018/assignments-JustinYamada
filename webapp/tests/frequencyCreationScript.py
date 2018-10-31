'''
    frequencyCreationScript.py
    Justin Hahn, 23 October 2018

    Code that creates a csv table by frequency of police codes
    using the Crime.csv file.
'''

import sys
import re
import csv

def load_from_crime_csv_file(csv_file_name):

    csv_file = open(csv_file_name, encoding='utf-8')
    print(csv_file_name)
    reader = csv.reader(csv_file)

    crime_frequency = {}
    code_to_crime = {}
    FirstRowSkip = True
    for row in reader:
        if FirstRowSkip == True:
            FirstRowSkip = False
            continue
        #assert len(row) == 26

        police_code = row[1]
        specific_crime = row[8]
        if police_code not in crime_frequency.keys():
            crime_frequency[police_code] = 1
            code_to_crime[police_code] = specific_crime
        else:
            crime_frequency[police_code] += 1

    csv_file.close()
    return (code_to_crime, crime_frequency)

def save_crime_frequency_table(code_to_crime, crime_frequency, csv_file_name):
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for key in sorted(crime_frequency, key=crime_frequency.get, reverse = True):
        row = [code_to_crime[key], key, crime_frequency[key]]
        writer.writerow(row)
    output_file.close()

if __name__ == '__main__':
    code_to_crime_dict, crime_frequency_dict = load_from_crime_csv_file('Crime.csv')
    save_crime_frequency_table(code_to_crime_dict, crime_frequency_dict, 'crime_frequency.csv')
