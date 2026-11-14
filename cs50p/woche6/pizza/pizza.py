import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

pizza = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizza.append(row)
        
except FileNotFoundError:
    sys.exit("File does not exist")


print(tabulate(pizza, headers="keys", tablefmt="grid"))

