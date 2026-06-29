import csv

file = open("Data/sales.csv", "r")
reader =csv.reader(file)

for row in reader:
    print(row)

file.close()