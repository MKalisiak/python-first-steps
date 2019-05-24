# Write a console text-based Reverse Number Wizard game
#
# In Number Wizard you pick a number between 1 and 100 in your head and the game is trying to guess it.
#
# We are going to create a Reverse Number Wizard, so you already might have an idea about what it should look like.
# The game picks a random number and the player is trying to guess it. With each guess the player gets a response
# telling him whether the chosen number is higher, lower or exactly equal to the guess.
#
#
# It should use argparse for the user to be able to set the bounds and difficulty level.
#
# The player should be able to use command line arguments to set the difficulty level of the game resulting in
# the maximum number of guesses before the player loses the game. Make it anything you like, for EXAMPLE:
# easy:   infinite tries
# medium: 7 tries
# hard:   3 tries
#
# The player should be able to use command line arguments to set the bounds of the set from which the game picks
# a random number (both inclusive).
#
# To pick a random integer number use 'randint(lower, upper)' function from 'random' module (example below).
# Example after the task, run this file to see it in action.
#
# After the player guesses correctly the game should print to the player how many tries did it take them.
# If a player loses they should also be notified of it.
# After the game ends it can ask the player if they want to play another round or the program may finish,
# that decision is up to you.
#
# GOOD LUCK and HAVE FUN :)

import random

print(random.randint(1, 100)) # both bounds are inclusive
