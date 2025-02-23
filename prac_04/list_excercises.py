def main():
    numbers = []  #empty list

    for i in range(5): #get 5 numbers
        number = int(input(f"Number: "))
        numbers.append(number)


    print(f"\nThe first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")  # Rounded to 1 decimal place

main()
