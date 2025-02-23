def main():
    check_username()
    numbers = []  #empty list

    for i in range(5): #get 5 numbers
        number = int(input(f"Number: "))
        numbers.append(number)


    print(f"\nThe first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")



def check_username():
    """Check if the user is in the authorized list of usernames."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("\nEnter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
