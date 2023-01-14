#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      caitl
#
# Created:     13/05/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
from turtle import *

def fibonacci():
    times = int(input("How many digits of the Fibonacci sequence would you like?"))
    fibonacci_sequence = [0,1] #Starts the list of fibonacci numbers.
    for i in range(times-2): #Loops around for 2 less than the number of digits asked for (2 digits are already in the list of digits).
        nextNumber = fibonacci_sequence[i] + fibonacci_sequence[i+1] #Gets the next number in the sequence by adding the last two together.
        fibonacci_sequence.append(nextNumber) #Adds it to the end of the list of digits.
    print (str(fibonacci_sequence)[1:-1]) #Prints the list of digits (without the brackets).
    reverse(fibonacci_sequence) #Goes to the reverse function.

def reverse(fibonacci_sequence):
    print(str(fibonacci_sequence[::-1])[1:-1]) #Prints the list of digits backwards.
    addition(fibonacci_sequence) #Goes to addition function.

def addition(fibonacci_sequence):
    total = 0 #Creates total variable.
    for i in range(len(fibonacci_sequence)): #For each digit in the list...
        total += fibonacci_sequence[i] #Adds the next digit to the total.
    print(total) #prints the value in total.
    turtle_setup(fibonacci_sequence) #Goes to turtle_setup function.

def turtle_setup(fibonacci_sequence):
    window = turtle.Screen() #Creates window
    window.title("Fibonacci spiral")
    terrance = turtle.Turtle() #Creates the turtle.
    terrance.hideturtle() #Hides the turtle.
    speed = terrance.speed(5) #Speeds up the turtle.
    draw(terrance,fibonacci_sequence) #Goes to draw function.

def square(terrance,side_length): #Creates a function to draw a square (using a loop).
    for i in range(4):
        terrance.forward(side_length)
        terrance.right(90)

def draw(terrance,fibonacci_sequence):
    numberOfSquares = len(fibonacci_sequence) #Uses the number of digits to to find the number of squares to draw.
    factor = 5 #enlargement factor.
    for i in range(numberOfSquares): #For each square...
        square(terrance,factor*fibonacci_sequence[i]) #Draws the square.
        terrance.penup() #Lifts the turtle/pen up.
        terrance.forward(factor*fibonacci_sequence[i]) #Goes forward the length of the square side.
        terrance.right(90) #Turns to face the right.
        terrance.forward(factor*fibonacci_sequence[i]) #Goes forward the length of the square side.
        terrance.pendown() #Puts the turtle/pen down.
    spiral(terrance,numberOfSquares,fibonacci_sequence,factor) #Goes to spiral function.

def spiral(terrance,numberOfSquares,fibonacci_sequence,factor):
    terrance.penup() #Lifts the turtle/pen up.
    terrance.goto(0,0) #Goes back to the start position.
    terrance.setheading(180) #Turns the turtle to face the right way.
    terrance.pencolor("green") #Changes the pen colour to green.
    terrance.pensize(3) #Changes the pen size.
    terrance.pendown() #Puts the turtle/pen down.
    for i in range(numberOfSquares): #For each of the sqaures...
        terrance.circle(-factor*fibonacci_sequence[i],90) #Draws a quarter of a circle that fits the square.

fibonacci()
