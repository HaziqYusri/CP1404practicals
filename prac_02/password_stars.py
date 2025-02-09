PASSWORD_LENGTH = 10

def main():

    password = get_password()

    asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password():
    password = input(f"Enter password of at least {PASSWORD_LENGTH} characters: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Enter password: ")
    return password


main()
