#Answer the following questions:
#1. When will a ValueError occur?
"""It occurs when the user input are not valid integers"""
#2. When will a ZeroDivisionError occur?
"""It occurs when a user attempts to put 0 in the denominator as it is impossible to divide by zero in mathematics."""
#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""In order to avoid a zero error we can first validate the user input before starting the calculation"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")