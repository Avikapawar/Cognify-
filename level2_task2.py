#task: Number Guesser

#Create a number guessing game where the
#program generates a random number
#between a specified range, and the user tries
#to guess it. Provide feedback to the user if
#their guess is too high or too low.
import random

lower_number = int(input("Enter the lower bound of the range: "))
upper_number = int(input("Enter the upper bound of the range: "))

secret_number = random.randint(lower_number, upper_number)

print(f"I'm thinking of a number between {lower_number} and {upper_number}.")


attempts = 0


while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid integer.")
