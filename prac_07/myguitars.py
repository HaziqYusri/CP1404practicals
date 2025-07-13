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
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar} added.\n")
        except ValueError:
            print("Invalid input. Year must be an integer, cost must be a number.")

    # Save all guitars back to file
    save_guitars("guitars.csv", guitars)
    print("Guitars saved to guitars.csv")

def load_guitars(filename):
    """Read guitars from the CSV and returns a list"""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(filename, guitars):
    """Writes guitars to CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

main()
