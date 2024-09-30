import csv

with open('std1.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)