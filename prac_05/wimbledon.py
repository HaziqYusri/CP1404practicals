"""
wimbledon.py
Estimate: 20 minutes
Actual:   minutes
"""
import csv

FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon_data(FILENAME)
    print(data)
    champions = count_champions(data)
    print(champions)
    countries = get_unique_countries(data)
    print(countries)

#Read the Wimbledon data and return a list of [champion, country].
def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            # Print to debug if necessary:
            # print(row)
            country = row[1].strip()
            champion = row[2].strip()
            data.append([champion, country])
    return data

#Count number of wins per champion and returns dictionary
def count_champions(data):
    champions_to_wins = {}
    for champion, _ in data:
        champions_to_wins[champion] = champions_to_wins.get(champion, 0) + 1
    return champions_to_wins

#Sort unique countries
def get_unique_countries(data):
    countries = {country for _, country in data}
    return sorted(countries)

main()