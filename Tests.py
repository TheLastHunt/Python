#Basic Calculator

#Basic Calculator

def calculate():
    num1 = int(input("Pick your first number"))
    sign = input("Pick the operation to be performed")
    num2 = int(input("Pick your second number"))

    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "/":
        print(num1/num2)

#calculate()

#Dice Roll Simulator

import random

def dice():
    reroll = True
    while reroll == True:
        roll = random.randint(1, 6)
        print(roll)
        ask = input("Do you want to roll again? Answer 'y' for Yes or 'n' for No.")
        if ask == "n":
            reroll = False


#dice()

#Dice Roll Improved

def roll():
    num = random.randint(1, 6)
    print(num)
    menu()


def menu():
    print(
        """
        1. Roll the dice
        
        2. Exit
        """
    )
    choice = int(input("Select an option:"))

    if choice == 1:
        roll()
    elif choice == 2:
        exit()

    
#roll()

#Guess The Word

def guess_the_word(word):
    correct = False
    guesses = 3
    while correct == False and guesses > 0:
        guess = input("Type your best guess:")
        if guess != word:
            guesses -= 1
            if guesses > 0:
                print("Try again!")
            else:
                print("Oops! You have ran out of guesses!")
        else:
            print("You got it!")
            correct = True
    

#guess_the_word()