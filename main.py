from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.geometry("700x400")
root.title("R,P,S Game")
root.config(bg = "lightblue")

playerScore = 0
computerScore = 0

options = [("rock",0),("paper",1),("scissors",2)]

def computerWins():
    global computerScore, playerScore
    computerScore += 1

    winnerL.config(text = "Computer Won!")
    computerScoreL.config(text = "Computer Score: " + str(computerScore))
    playerScoreL.config(text = "Player Score: " + str(playerScore))

def playerWins():
    global playerScore, computerScore
    playerScore += 1

    winnerL.config(text = "Player Won!")
    playerScoreL.config(text = "Player Score: " + str(playerScore))
    computerScoreL.config(text = "Computer Score: " + str(computerScore))

def tie():
    global playerScore, computerScore

    winnerL.config(text = "Tie!")
    playerScoreL.config(text = "Player Score: " + str(playerScore))
    computerScoreL.config(text = "Computer Score: " + str(computerScore))

def getCompChoice():
    return random.choice(options)

def getPlayerChoice(playerInput):
    global computerScore, playerScore
    computerInput = getCompChoice()

    playerChoiceL.config(text = "You selected: " + playerInput[0])
    computerChoiceL.config(text = "Computer selected: " + computerInput[0])

    if playerInput == computerInput:
        tie()

    if(playerInput[1] == 0):
        if (computerInput[1] == 1):
            computerWins()
        elif (computerInput[1] == 2):
            playerWins()

    elif (playerInput[1] == 1):
        if (computerInput[1] == 0):
            playerWins()
        elif (computerInput[1] == 2):
            computerWins()

    elif (playerInput[1] == 2):
        if (computerInput[1] == 0):
            computerWins()
        elif (computerInput[1] == 1):
            playerWins()


title = Label(root, text = "Rock, Paper, Scissors", font = font.Font(size = 20), fg = "grey")
title.pack(pady = 10)

winnerL = Label(root, text = "Start the Game", fg = "green", font = font.Font(size = 12))
winnerL.pack(pady = 10)

topFrame = Frame(root)
topFrame.pack(pady = 30)

topFrame.config(bg = "lightblue")

userOpt = Label(topFrame, text = "Your Options:", fg = "grey", font = font.Font(size = 15))
userOpt.grid(row = 0, column = 0, pady = 10)

userRock = Button(topFrame, text = "Rock", bg = "pink", width = 20, height = 2, bd = 0, command = lambda: getPlayerChoice(options[0]))
userRock.grid(row = 2, column = 1)

userPaper = Button(topFrame, text = "Paper", bg = "lightgrey", width = 20, height = 2, bd = 0, command = lambda: getPlayerChoice(options[1]))
userPaper.grid(row = 2, column = 2, padx = 40)

userScissors = Button(topFrame, text = "Scissors", bg = "lightgreen", width = 20, height = 2, bd = 0, command = lambda: getPlayerChoice(options[2]))
userScissors.grid(row = 2, column = 3)

bottomFrame = Frame(root)
bottomFrame.pack()

bottomFrame.config(bg = "lightblue")

score = Label(bottomFrame, text = "Score", fg = "grey", font = font.Font(size = 15))
score.grid(row = 0, column = 0)


playerChoiceL = Label(bottomFrame, text = "You Selected: --------", font = font.Font(size = 12))
playerChoiceL.grid(row = 1, column = 1, padx = 20)

playerScoreL = Label(bottomFrame, text = "Player Score: --------", font = font.Font(size = 12))
playerScoreL.grid(row = 1, column = 2, pady = 20)

computerChoiceL = Label(bottomFrame, text = "Computer Selected: --------", font = font.Font(size = 12))
computerChoiceL.grid(row = 2, column = 1, padx = 20)

computerScoreL = Label(bottomFrame, text = "Computer Score: --------", font = font.Font(size = 12))
computerScoreL.grid(row = 2, column = 2)


root.mainloop()