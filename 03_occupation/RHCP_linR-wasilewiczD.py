import csv

def randomoccup():
    with open('occupations.csv') as csv_file:
        csv_reader = csv.reader(csv_file, )
