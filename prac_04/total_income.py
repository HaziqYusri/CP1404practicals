"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

"""
def main():
    #Display income report for incomes over a given number of months
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
"""

def main():
    """Display income report for incomes over a given number of months."""
    months = int(input("How many months? "))
    incomes = get_income_list(months)
    print_income_report(incomes, months)


def get_income_list(months):
    """Gets the list of incomes from user input."""
    incomes = []
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes, months):

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
