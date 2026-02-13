#Task: Guessing Game
#Write a Python program that generates a
#random number between 1 and 100. The
# should then try to guess the number.
#The program should provide hints such as
#"too high" or "too low" until the correct
#number is guessed.` 

import random
random_number=random.randint(1,100) 

print("Welcome!! Take Guess Between Number 1 to 100:")
print("Let's Whether You get Correct Guess of Number!!")

while True:
    user=int(input("Enter Random Number Between 1 to 100::"))

    if user>random_number:
        print("Too High!!")
    elif user<random_number:
        print("Too Low!!") 
    else:
        print("Congratulations! You guessed the correct number!")
        break
    