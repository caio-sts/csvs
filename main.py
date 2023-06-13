import csv

with open('empresa_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) != 0 and row[6] != "":
            print(row)