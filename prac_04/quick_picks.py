import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    #no. of quick picks
    no_of_picks = int(input("How many quick picks would you like to generate? "))
    while no_of_picks < 0:
        print("Invalid input try again")
        no_of_picks = int(input("How many quick picks would you like to generate? "))

    for i in range(no_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    quick_pick = set()

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.add(number) #unique generated

    return sorted(quick_pick)

main()
