import csv

csv.register_dialect(
    'my_dialect',
    delimiter='|',
    quoting=csv.QUOTE_MINIMAL,
    skipinitialspace=True
)

with open('std2.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='my_dialect')
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 23, 'New York'])
    writer.writerow(['Name', 30, 'Los Angeles'])

with open('std2.csv', 'r') as file:
    reader = csv.reader(file, dialect='my_dialect')
    for row in reader:
        print(row)