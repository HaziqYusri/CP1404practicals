"""
wimbledon.py
Estimate: 25 minutes
Actual:  minutes
"""

FILENAME = "wimbledon.csv"
#Read the Wimbledon data and return a list of [champion, country].
def read_wimbledon_data(filename):

    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            year, country, champion = line.strip().split(",")
            data.append([champion, country])
    return data

def main():
    data = read_wimbledon_data(FILENAME)

if __name__ == '__main__':
    main()