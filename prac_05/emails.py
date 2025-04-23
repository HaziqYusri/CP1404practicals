"""
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""

#Extract and format a guessed name from the email.
def extract_name(email):
    parts = email.split('@')[0].split('.')
    name = ' '.join(part.title() for part in parts)
    return name

#Main code to collect and process names
def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        #Guess a name from the email
        name_guess = extract_name(email)
        confirmation = input(f"Is your name {name_guess}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y"):
            name_guess = input("Name: ").strip()

        email_to_name[email] = name_guess

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == '__main__':
    main()