""" == Number guessing game in python == """

import random

print(" == Number guessing Game == \n")

try:
    low  = int(input("Enter the lower bound : "))
    high = int(input("Enter the upper bound : "))
    print(f"""\nYou will get only 7 chances to 
guess the correct number between {low} and {high}\n""")
    num = random.randint(low,high)
    steps = 0
    invalid = 0
    while steps <= 7:
        guess = int(input ("Enter the number : "))
        if guess == num:
            steps += 1
            print(f"\nHooray! your guess was correct in {steps} steps ")
            break
        else:
            if guess < low or guess > high:
                print(f"Invalid guess : Enter the number between {low} and {high}")
                invalid += 1
            else:
                print("Too low" if guess < num else "Too High")
                steps += 1
    else:
        print(f"The number was {num}, better luck next time")
except Exception as e:
    print(f"Invalid input : {e}")
finally:
    if invalid > 0:
        print(f"Invalid guesses : {invalid}")
        print(f"Valid Guesses : {steps}")
        print(f"Total Guesses : {steps + invalid}")
    else:
        print(f"Total Guesses : {steps}")