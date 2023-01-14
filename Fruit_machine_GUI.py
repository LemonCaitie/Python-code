#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     07/04/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#________________________________________________________________________#
from tkinter import *
import random

credit = 100 #The players initial credit isn't assigned in the menu fuction otherwise it would be reassigned every turn.
#________________________________________________________________________#
def start(): #The menu is where every turn starts
    global credit
    total.delete(0.0,END) #This section empties the boxes so they can be populated in the new turn
    winnings.delete(0.0,END)
    pullOne.delete(0.0,END)
    pullTwo.delete(0.0,END)
    pullThree.delete(0.0,END)
    if credit >= 20: #Checks to see if the player has enough money for a turn.
        game()#Goes to game function
    else: #If the player doesn't have enough credit the program ends after the print statement.
        end()#Goes to end function
#________________________________________________________________________#
def end():#makes the GUI shwo the 'end screen'
    global credit
    winnings.delete(0.0,END)
    if credit <= 20: #checks to see if their walking away or have run out of money
        winnings.insert(END,"Bust!")
    else:
        winnings.insert(END,"Bye!")
#________________________________________________________________________#
def game(): #This function is the centre of the game.
    global credit
    symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]
    credit -= 20
    #These three statements choose random symbols for each 'reel'
    rollOne = str(random.choice(symbols))
    rollTwo = str(random.choice(symbols))
    rollThree = str(random.choice(symbols))
    #________________________________________________________________________#
    #Finds out if all the symbols are the same
    if rollOne == rollTwo:
        if rollOne == rollThree:
            trpl(rollOne,rollTwo,rollThree)
        else:#Finds out if isn't not a triple, if it's a double and if the double is a skull
            if rollOne == "Skull":
                dblSkull(rollOne,rollTwo,rollThree)#If it's a double skull, it goes to a separate function
            else:
                dbl(rollOne,rollTwo,rollThree)#If it's any other symbol, the same thing happens, so goes to a different function
    #________________________________________________________________________#
    #Finds out if any other two of the symbols are the same and if it's a double skull
    elif rollTwo == rollThree:
        if rollTwo == "Skull":
                dblSkull(rollOne,rollTwo,rollThree)#If it's a double skull, it goes to a separate function
        else:
            dbl(rollOne,rollTwo,rollThree)#If it's any other symbol, the same thing happens, so goes to a different function
    elif rollOne == rollThree:
        if rollOne == "Skull":
                dblSkull(rollOne,rollTwo,rollThree)#If it's a double skull, it goes to a separate function
        else:
            dbl(rollOne,rollTwo,rollThree)#If it's any other symbol, the same thing happens, so goes to a different function
    #________________________________________________________________________#
    else: #If none of the symbols are the same...
        win="£0"
        upDateWindow(rollOne,rollTwo,rollThree,win)
#________________________________________________________________________#
def trpl(rollOne,rollTwo,rollThree): #Says what happens if all the symbols are the same.
    global credit
    if rollOne == "Skull": #If it's a triple skull...
        credit = 0
        win="000"
        upDateWindow(pullOne,pullTwo,pullThree,win)
        end()
    elif rollOne == "Bell":#If it's a triple bell...
        credit += 500
        win="£5"
        upDateWindow(rollOne,rollTwo,rollThree,win)
    else: #If it's a triple of any other symbol...
        credit += 100
        win="£1"
        upDateWindow(rollOne,rollTwo,rollThree,win)
#________________________________________________________________________#
def dbl(rollOne,rollTwo,rollThree): #Says what happens if two of the symbols are the same.
    global credit
    credit += 50
    win="50p"
    upDateWindow(rollOne,rollTwo,rollThree,win)
#________________________________________________________________________#
def dblSkull(rollOne,rollTwo,rollThree): #If it's a double skull...
    global credit
    win="-£1"
    if credit > 100: #Checks to see if the 'roll' has made the player go bust
        credit -= 100
        upDateWindow(rollOne,rollTwo,rollThree,win)
    else:
        credit = 0
        upDateWindow(rollOne,rollTwo,rollThree,win)
        end()
#________________________________________________________________________#
def upDateWindow(rollOne,rollTwo,rollThree,win): #Makes the GUI show the relevant information from the 'turn/roll'
    global credit
    displayCredit = credit/100 #Makes the credit look correct to the user (There were issues with the maths when I make it a float for the whole program)
    displayCredit = "£"+ str(displayCredit) +"0" #Makes the credit a string to put in the GUI box.
    pullOne.insert(END,rollOne) #Updates the 'reels'
    pullTwo.insert(END,rollTwo)
    pullThree.insert(END,rollThree)
    winnings.insert(END,win) #Updates the winnign for that round
    total.insert(END,displayCredit[0:5]) #Updates the credit box
#________________________________________________________________________#
#Makes the GUI
window = Tk()
window.title("Fruit Machine")

Label(window,text="\nFruit Machine!",).grid(row=3,column=3)

Label(window,text="\nYou win:",).grid(row=6,column=3)
winnings= Text(window, width=10, height=2, wrap=WORD,bg="yellow")
winnings.grid(row=7, column=3,columnspan=3,rowspan=2,sticky=W,padx=4,pady=2)

Label(window,text="\nTotal:",).grid(row=9,column=3)
total = Text(window, width=10, height=2, wrap=WORD,bg="yellow")
total.grid(row=11, column=3,columnspan=3,rowspan=2,sticky=W,padx=4,pady=2)
total.insert(END,"£1")

pullOne = Text(window, width=10, height=6, wrap=WORD,bg="yellow")
pullOne.grid(row=4, column=0,columnspan=3,rowspan=2,sticky=W,padx=4,pady=2)

pullTwo = Text(window, width=10, height=6, wrap=WORD,bg="yellow")
pullTwo.grid(row=4, column=3,columnspan=3,rowspan=2,sticky=W,padx=4,pady=2)

pullThree = Text(window, width=10, height=6, wrap=WORD,bg="yellow")
pullThree.grid(row=4, column=6,columnspan=3,rowspan=2,sticky=W,padx=4,pady=2)

s = 'Spin!'
Button(window, text = s,width=10,command=start).grid(row=6,column=2,sticky=S,padx=4,pady=2)

l = 'Walk away'
Button(window, text = l,width=10,command=end).grid(row=6,column=7,sticky=S,padx=4,pady=2)

window.mainloop()#Starts the program
