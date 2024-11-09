# Number Guesser Feature
import random

def number_guesser():
    correct_number = random.randint(1, 10)
    attempts = 3
    
    print("Welcome to Number Guesser!")
    for attempt in range(attempts):
        user_guess = int(input("Guess the number between 1 and 10: "))
        if user_guess == correct_number:
            print("Correct! You've guessed the number!")
            return
        elif user_guess < correct_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    
    print(f"Sorry, you've used all attempts. The correct number was {correct_number}.")

# Example usage
number_guesser()
