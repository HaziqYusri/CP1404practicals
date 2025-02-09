from score import score_rating  # Assuming score.py is in the same directory

def get_valid_score():
    """Gets a valid score (0-100) from the user."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_result(score):
    rating = score_rating(score)
    print(f"Result: {rating}")

def show_stars(score):
    print("*" * int(score))

def main():
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")

main()