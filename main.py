import csv

def display_title():
    print("=" * 50)
    print("     SALES ANALYTICS SYSTEM")
    print("=" * 50)

display_title()

file = open("Data/sales.csv", "r")

reader =csv.reader(file)
next(reader)

total_revenue = 0 

for row in reader:

    quantity = int(row[5])
    price = int(row[6])
    revenue = quantity * price

    total_revenue += revenue
    
    print("=" * 50)
    print("Order ID      :", row[0])
    print("Date          :", row[1])
    print("Customer Name :", row[2])
    print("Product       :", row[3])
    print("Category      :", row[4])
    print("Quantity      :", row[5])
    print("Price         : ₹", row[6])
    print("Revenue       : ₹", revenue)
    
print("=" * 50)
print("Total Revenue : ₹", total_revenue)

file.close()