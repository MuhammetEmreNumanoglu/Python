import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Guess the number (1-100)! You have", max_attempts, "attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            return

    print(f"Game over! The number was {secret}.")

number_guessing_game()
