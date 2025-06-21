"""
CP1404 Practical 5
Hexadecimal colour lookup
"""

# Dictionary of 10 colours
HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

# Display all available color names
for name, code in HEX_COLOURS.items():
    print(f"{name.capitalize():<20} is {code}")

#User input loop
colour_name = input("Enter a colour name: ").lower()

while colour_name != "":
    hex_code = HEX_COLOURS.get(colour_name)
    if hex_code:
        print(f"The code for \"{colour_name}\" is {HEX_COLOURS.get(colour_name)}")
        colour_name = input("Enter a colour name: ").lower()
    else:
        print("Invalid colour, please try again.")
        colour_name = input("Enter a colour name: ").lower()

print("Goodbye!")