#!python3
# a rock-paper-scissors program that gets better the more it's played
# main game program

import random
import shelve
from rpsHelper import *

def main():
    # open shelves
    playerData = shelve.open("playerdata")
    botData = shelve.open("botdata")
    # initialize botdata
    if "wins" not in list(botData.keys()):
        botData["wins"] = 0
        botData["losses"] = 0
    # game variables
    round = 0
    botWins = 0
    humanWins = 0
    prevWinner = ""
    prevMove = ""
    reps = False
    # check-in
    firstName = input("What's your first name? ")
    lastName = input("What's your last name? ")
    player = firstName + lastName
    if player in list(playerData.keys()):
        print("Welcome back, " + firstName + "!")
    else:
        print("Welcome, " + firstName + "!")
        playerData[player] = [0, 0, 0]
    history = list(playerData[player])
    # set round limit
    roundLimit = int(input("How many rounds would you like to play? "))
    # gameplay
    humanDecision = ""
    while round < roundLimit:
        print("Round " + str(round + 1) + ":")
        print("Bot wins: " + str(botWins) + " Human wins: " + str(humanWins))
        botDecision = botChoice(round, history, prevWinner, prevMove, reps)
        while humanDecision not in moveset:
            humanDecision = input("Please enter \"rock\", \"paper\", or \"scissors\" ")
        # update database
        playerData[player][moveset.index(humanDecision)] += 1
        # check for repeats
        if humanDecision == prevMove:
            reps = True
        else:
            reps = False
            prevMove = humanDecision
        # compare
        print("bot plays " + botDecision)
        winner = compare(botDecision, humanDecision)
        if winner == "bot":
            print("Bot wins!")
            prevWinner = "bot"
            botData["wins"] += 1
            botWins += 1
        elif winner == "human":
            print("You win!")
            prevWinner = "human"
            botData["losses"] += 1
            humanWins += 1
        else:
            print("Tie!")
        round += 1
        humanDecision = ""
        print()
    # announce result
    print("Bot wins: " + str(botWins) + " Human wins: " + str(humanWins))
    if botWins > humanWins:
        print("Defeat.")
    elif botWins < humanWins:
        print("Victory!")
    else:
        print("Draw.")
    # announce all time bot performance
    allTimeWinRate = float(botData["wins"]) / (botData["wins"] + botData["losses"])
    print("All time bot win-rate = " + str(allTimeWinRate))
    # close shelves
    playerData.close()
    botData.close()

if __name__ == "__main__":
    main()
