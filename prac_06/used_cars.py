"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    #Initialise limo with 100 fuel
    limo = Car("Limo", 100)

    #Add 20 units of fuel
    limo.add_fuel(20)

    #Print current fuel units
    print(f"Limo has {limo.fuel} units of fuel.")

    #Drive 115km
    limo.drive(115)

    #Print ___str___
    print(limo)


main()