import csv

data = [
    ['Name', 'Age', 'City'],
    ['Uday', 20, 'Shapur'],
    ['Mihir', 21, 'Manglore'],
    ['Darshit', 22, 'Junagadh'],
]

with open('std1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)