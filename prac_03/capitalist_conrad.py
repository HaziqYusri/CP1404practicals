import random

#TODO: Updating constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00 #min price update (prev 0.01)
MAX_PRICE = 100.00 #max price update (prev 1000.0)
INITIAL_PRICE = 10.0
OUTPUT_FILE = "capitalist.txt"

price = INITIAL_PRICE
print(f"${price:,.2f}")
number_of_days = 0

# Open file for writing
out_file = open(OUTPUT_FILE, 'w')

# Write initial price
out_file.write(f"Starting price: ${price:,.2f}\n")
print(f"Starting price: ${price:,.2f}")


while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"${price:,.2f}")


    out_file.write(f"On day {number_of_days} price is: ${price:,.2f}\n")
    print(f"On day {number_of_days} price is: ${price:,.2f}")


out_file.close()
