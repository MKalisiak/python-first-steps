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


import argparse
import random
import math
import sys

# Note that it could have been done completely differently, it's just my take on the problem
parser = argparse.ArgumentParser(prog='reverse_number_wizard', description='Play Reverse Number Wizard with custom ruleset.')
parser.add_argument('-l', '--lower', type=int, default=1, help='lower bound')
parser.add_argument('-u', '--upper', type=int, default=100 , help='upper bound')
parser.add_argument('-d', '--difficulty', type=str, default='easy', help='difficulty should be one of {easy, medium, hard}')

args = parser.parse_args()

difficulty_levels = {
    'easy': math.inf,
    'medium': math.ceil(math.log(args.upper - args.lower + 1, 2)),
    'hard': math.floor(math.log(args.upper - args.lower + 1, 2) / 2)
}

if args.difficulty not in difficulty_levels:
    print(f"Unknown difficulty level - {args.difficulty}", file=sys.stderr)
    parser.print_help(file=sys.stderr)
    exit(1)

def prompt_to_play_again():
    answer = input("Want to play again? (y/N)")
    if answer.lower().startswith('y'):
        chosen_number = random.randint(args.lower, args.upper)
        guess_count = 0
        return chosen_number, guess_count, True
    else:
        return None, None, False

chosen_number = random.randint(args.lower, args.upper)

guess_count = 0

print("Welcome! I am the Great and Powerful Reverse Number Wizard!")
print(f"I have chosen a number between {args.lower} and {args.upper}.")
print(f"Try to guess it. "
      f"You have {difficulty_levels[args.difficulty] if difficulty_levels[args.difficulty] != math.inf else 'infinite'} tries")

while True:
    guess = input("Your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Only numbers please")
        continue

    guess_count += 1

    if guess == chosen_number:
        print("I admit I am impressed you managed to guess it.")
        chosen_number, guess_count, play_again = prompt_to_play_again()
        if play_again:
            continue
        else:
            print("Next time I will not lose")
            exit(0)

    if guess_count >= difficulty_levels[args.difficulty]:
        print("I knew you were too weak to do it. I am not even sorry for you, mortal.")
        chosen_number, guess_count, play_again = prompt_to_play_again()
        if play_again:
            continue
        else:
            print("That was expected, cower in fear before my power")
            exit(0)

    if guess < chosen_number:
        print(random.choice(["My number is higher", "That is too low", "Do mortals only know such low numbers?"]))

    else:
        print(random.choice(["My number is lower", "That is too high", "What, do you think I have something to compensate for? Lower..."]))
