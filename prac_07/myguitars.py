import csv
from guitar import Guitar

def main():
    """Read guitars from CSV, sorts by year then displays them."""
    print("My guitars!")
    guitars = load_guitars("guitars.csv")

    guitars.sort() #Uses __lt__

    print("\nThese are my guitars (sorted by year):")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    #Lets user add new guitars
    print("\nAdd new guitars:")

    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

def load_guitars(filename):
    """Read guitars from the CSV and returns a list"""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

main()
