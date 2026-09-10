import random

def guessing_game():

    print("\n----- Number Guessing Game -----")
    print("Guess a number between 1 and 100")
    print("You have 5 attempts.")

    secret_number = random.randint(1, 100)

    attempts = 5
    score = 100

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{attempts}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                print("\nCongratulations!")
                print("You guessed the correct number.")
                print("Your score:", score)
                return

            elif guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

            score -= 20

        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Your score:", score)

while True:

    guessing_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break