import csv

print("=" * 50)
print("     SALES ANALYTICS SYSTEM")
print("=" * 50)

file = open("Data/sales.csv", "r")

reader =csv.reader(file)
next(reader)

for row in reader:
    print("=" * 50)

    print("order Id      :", row[0])
    print("Date          :", row[1])
    print("Customer Name :", row[2])
    print("Product       :", row[3])
    print("Category      :", row[4])
    print("Quantity      :", row[5])
    print("Price         :", row[6])

file.close()