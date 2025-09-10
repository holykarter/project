''' use different algorithm to make a guessing game , and see which get the answer faster , 
make different implemetation ,'''

# noobie version 
# A simple number guessing game

number = 46
user_guess = 0  # Initialize user_guess to a number that is not correct

# Loop until the user guesses the correct number
while user_guess != number:
    try:
        user_guess_str = input("Guess a number between 1 and 100: ")
        user_guess = int(user_guess_str)
    except ValueError:
        print("That's not a valid number! Please guess again.")
        continue  # Skip to the next iteration of the loop

    # Check if the guess is within the valid range
    if not (1 <= user_guess <= 100):
        print("Your guess is outside the valid range. Please guess a number between 1 and 100.")

    # Check the user's guess against the correct number
    elif user_guess < number:
        print("Your guess is too low. Guess again!")
    
    elif user_guess > number:
        print("Your guess is too high. Guess again!")

    else:
        print("Congratulations! You guessed the right number!")

''' -----------------second part code-------------------------------- '''
# import random

import random
def binary_search(target, low, high):
        guess = 0
 # i don't make a copy because there are non mutable type val (low,high)
        while low <= high:
                mid = (low + high ) // 2
                guess += 1
                print(mid)
                if mid  == target:
                        return guess
                elif mid < target:
                        low = mid + 1
                else:
                        high = mid - 1
        return None

target = random.randint(1,100000)

binary_search(target,1, 100000)
