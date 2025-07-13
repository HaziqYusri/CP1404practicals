from guitar import Guitar

def main():
    """Testing guitar class"""
    g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    g2 = Guitar("Another Guitar", 2013, 500)

    print(f"{g1.name} get_age() - Expected 100. Got {g1.get_age()}")
    print(f"{g2.name} get_age() - Expected 9. Got {g2.get_age()}")

    print(f"{g1.name} is_vintage() - Expected True. Got {g1.is_vintage()}")
    print(f"{g2.name} is_vintage() - Expected False. Got {g2.is_vintage()}")

main()