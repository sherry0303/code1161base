"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nwelcome to the guessing game!")
    print("A number between _ and _ ?")

    # while True:
    #     lowerBound = not_number_rejector("Please give me a lower bound: ")
    #     upperBound = not_number_rejector("Please give me an upper bound: ")
    #     if lowerBound > upperBound:
    #         print ("Lower bound should be smaller than upper bound.")
    #         continue
    #     else:
    #         break
    lowerBound = not_number_rejector("Please give me a lower bound: ")

    while True:
        upperBound = not_number_rejector("Please give me an upper bound: ")
        if lowerBound < upperBound + 1:
            break

    print("OK then, a number between {} and {} ?".format(lowerBound,
          upperBound))

    # lowerBound = int(lowerBound)
    # upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)
    print (actualNumber)

    guessed = False

    while not guessed:
        guessedNumber = super_asker(lowerBound, upperBound)
        print("you guessed {},".format(guessedNumber))
        if guessedNumber not in range(lowerBound, upperBound + 1):
            print("The gussed number is not between {} and {}."
                  .format(lowerBound, upperBound))
        elif guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
