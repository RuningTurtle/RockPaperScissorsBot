#!python3
# a rock-paper-scissors program that gets better the more it's played
# helper functions for the main program

import random
import shelve

moveset = ("rock", "paper", "scissors")

# comparison function
def compare(a, b):
    if moveset.index(a) == (moveset.index(b) + 1) % 3:
        return "bot"
    elif moveset.index(b) == (moveset.index(a) + 1) % 3:
        return "human"
    else:
        return "tie"

# decision tree for bot
def botChoice(round, history, prevWinner, prevMove, reps):
    # first round random choice
    if round == 0:
        return random.choice(moveset)
    # predict repetition avoidance
    if reps and random.random() < 0.77:
        if prevWinner == "human":
            return moveset[(moveset.index(prevMove) + 1) % 3]
        elif prevWinner == "bot":
            return moveset[(moveset.index(prevMove) + 2) % 3]
    # predict repetition / predict
    if prevWinner == "human" and random.random() < 0.77:
        return moveset[(moveset.index(prevMove) + 1) % 3]
    elif prevWinner == "bot" and random.random() < 0.77:
        return moveset[(moveset.index(prevMove) + 2) % 3]
    # weighted choice if all else fails
    total = history[0] + history[1] + history[2]
    randNum = random.randrange(total + 1)
    if randNum < history[0]:
        return moveset[1]
    elif randNum < history[0] + history[1]:
        return moveset[2]
    else:
        return moveset[0]
