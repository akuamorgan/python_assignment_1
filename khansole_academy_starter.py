"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.



import random
use code below  to generate a random integer between 30 and 50 for example
print(random.randint(30, 50))

"""

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

import random

# initialization
random_min = 10
random_max = 99
breaker = 1

while breaker < 4:                                                                      # while loop
    first_random_number = random.randint(random_min, random_max)                        # generate first random number
    second_random_number = random.randint(random_min, random_max)                       # generate second random number
    answer = first_random_number + second_random_number                                 # sum of random numbers

    output_text = "What is {} + {}? "
    user_input = input(output_text.format(first_random_number, second_random_number))   # user inputs the sum

    if user_input.isnumeric() is True:
        user_input_to_int = int(user_input)                                             # convert input string to int
        if user_input_to_int == answer:                                                 # if statement
            print("Your Answer: " + user_input)
            text = "Correct! You have gotten {} correct in a row "
            print(text.format(breaker))
            breaker += 1                                                                # increment to terminate loop
        else:
            print("Your Answer: " + user_input)
            print("Incorrect. The expected answer is " + str(answer))
            breaker = 1                                                                 # resets breaker to 1
    else:
        print("Please enter a number")

print("Congratulations, You have mastered addition")
