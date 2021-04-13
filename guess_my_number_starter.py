"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
import random
use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))
"""
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

import random
random_number = random.randint(1, 99)
print("I am thinking of a number between 1 and 99")

while True:                                         # loop to keep the program running until guess is correct
    user_input = input("Enter a guess ")            # accepts user's guess

    if user_input.isnumeric() is True:              # checks if input string contains a number
        user_input_to_int = int(user_input)         # convert input string to an integer
        if user_input_to_int > random_number:       # checks if user input is greater than random number
            print("Your guess is too high")
        elif user_input_to_int < random_number:     # checks if user input is less than random number
            print("Your guess is too small")
        elif user_input_to_int == random_number:    # output for a correctly guessed number
            text = "Congrats! The number was: {}"
            print(text.format(random_number))
            break                                   # exit while loop
    else:
        print("Please enter a number")

