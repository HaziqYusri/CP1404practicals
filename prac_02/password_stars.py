PASSWORD_LENGTH = 10

password = input(f"Enter password of at least {PASSWORD_LENGTH} characters: ")
while len(password) <= PASSWORD_LENGTH:
    print("Invalid Password")
    password = input("Enter password: ")


print('*' * len(password))
