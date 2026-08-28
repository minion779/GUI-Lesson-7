from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.geometry("700x400")
root.title("R,P,S Game")
root.config(bg = "lightblue")

title = Label(root, text = "Rock, Paper, Scissors", font = font.Font(size = 20), fg = "grey")
title.pack()

winner = Label(root, text = "Start the Game", fg = "green", font = font.Font(size = 12))
winner.pack()

topFrame = Frame(root)
topFrame.pack(pady = 50)

topFrame.config(bg = "lightblue")

userOpt = Label(topFrame, text = "Your Options:", fg = "grey", font = font.Font(size = 15))
userOpt.grid(row = 0, column = 0, pady = 10)

userRock = Button(topFrame, text = "Rock", bg = "pink", width = 20, height = 2, bd = 0)
userRock.grid(row = 2, column = 1)

userPaper = Button(topFrame, text = "Paper", bg = "lightgrey", width = 20, height = 2, bd = 0)
userPaper.grid(row = 2, column = 2, padx = 40)

userScissors = Button(topFrame, text = "Scissors", bg = "lightgreen", width = 20, height = 2, bd = 0)
userScissors.grid(row = 2, column = 3)

bottomFrame = Frame(root)
bottomFrame.pack()

bottomFrame.config(bg = "lightblue")

score = Label(bottomFrame, text = "Score", fg = "grey", font = font.Font(size = 15))
score.grid(row = 0, column = 0)


playerChoice = Label(bottomFrame, text = "You Selected: --------", font = font.Font(size = 12))
playerChoice.grid(row = 1, column = 1, padx = 20)

playerScore = Label(bottomFrame, text = "Player Score: --------", font = font.Font(size = 12))
playerScore.grid(row = 1, column = 2, pady = 20)

ComputerChoice = Label(bottomFrame, text = "Computer Selected: --------", font = font.Font(size = 12))
ComputerChoice.grid(row = 2, column = 1, padx = 20)

ComputerScore = Label(bottomFrame, text = "Computer Score: --------", font = font.Font(size = 12))
ComputerScore.grid(row = 2, column = 2)


root.mainloop()