# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

# widget : count
counts = {}
largest_day = [0, 0, 0, 0, 0]
average_amount = 0

with open("sales.csv", "r") as sales:
    next(sales)

    i = 0
    for line in sales:
        i = i + 1
        row = line.split(',')

        average_amount = average_amount + int(row[2])

        if counts.get(row[1]):
            counts[row[1]] += 1
        else:
            counts[row[1]] = 1

        if int(row[2]) > int(largest_day[2]):
            largest_day = row

    average_amount = average_amount / i;
    print(f"Highest Selling Widget: {max(counts, key=counts.get)}")
    print(f"Average Widget sold for: £{average_amount}")
    print(f"Largest selling day: {largest_day[0]}")


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows