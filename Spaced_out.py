#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitlin
#
# Created:     09/04/2020
# Copyright:   (c) caitlin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle #I had to change the import statement for my version of python, as I got 'NameError: name 'turtle' is not defined'
from tkinter import *
import random
#Creates the window and the turtles needed for the drawing.
window = turtle.Screen()
window.bgcolor("black")
window.title("Turtle")
window.screensize(900,700)
horace = turtle.Turtle()
horace.hideturtle()
horace.pencolor("white")
speed = horace.speed(5000)

don = turtle.Turtle()
don.speed(0)
don.width(3)
don.hideturtle()

def star(turtle,speed):
    size = random.randint(1,4) #creates a random number for the size of the star.
    x = random.randint(-700,700) #creates random coordinates.
    y = random.randint(-500,500)
    horace.penup()
    horace.goto(x,y) #moves the turtle to the random coordinates without drawing anything (penup and pendown).
    horace.pendown()
    angle = 120
    horace.fillcolor("white") #Makes all the stars white.
    horace.begin_fill()
    #Draws the star...
    for side in range(5):
        horace.forward(size)
        horace.right(angle)
        horace.forward(size)
        horace.right(72 - angle)
    horace.end_fill()

def planet(turtle,speed):
    x = random.randint(-600,600) #Creates random coordinates for the planet.
    y = random.randint(-300,300)
    horace.penup()
    horace.goto(x,y)#Moves the turtle to the random coordinates without drawing anything (penup and pendown).
    horace.pendown()
    colours = ["blue","red","yellow","green","pink"] #Creates a list of colours that the planets could be.
    horace.pencolor(random.choice(colours)) #Randomly selects a colour for the planet.
    size = random.randint(50,100) #Makes the size for the planet randomly.
    horace.dot(size)#draws the planet.
    if bool(random.getrandbits(1)) == True: #Randomly decides if the planet has a ring or not.
        #draws a white 'ring' on the planet.
        horace.pensize(6)
        horace.pencolor("white")
        horace.penup()
        horace.goto(x,y)
        horace.pendown()
        horace.forward(size*0.75)
        horace.right(180)
        horace.forward(size*1.5)

def milkyWay(horace):
    x = random.randint(-600,600)#Creates random coordinates for the milky way.
    y = random.randint(-300,300)
    horace.penup()
    horace.goto(x,y)#Moves the turtle to the random coordinates without drawing anything (penup and pendown).
    horace.pendown()
    s = random.randint(3,15)
    #Draws a spiral of dots for the milky way.
    for i in range(30):
        horace.dot(4)
        horace.penup()
        horace.forward(s+i)
        horace.pendown()
        horace.left(30 - i/1.5)

def draw_Spaceship():
    draw_Oval() #Goes to a function to draw the base of the UFO.
    draw_SemiCircle() #Goes to a function to draw the top of the UFO.
    window.tracer(1)

def draw_Oval():
    don.color('light grey') #Sets the colour of the outline.
    don.fillcolor("light grey") #Sets the colour of the fill.
    don.seth(-45) #Angles the turtle correctly
    #Draws the base...
    don.begin_fill()
    don.circle(28,90)
    don.circle(3,90)
    don.circle(28,90)
    don.circle(3,90)
    don.end_fill()
    don.seth(0)

def draw_SemiCircle():
    don.color('gold') #Sets the colour of the outline.
    don.fillcolor("gold") #Sets the colour of the fill.
    #Places the top in the right place in relation to the base.
    don.penup()
    don.forward(32)
    don.left(90)
    don.forward(10)
    don.right(90)
    don.pendown()
    #Draws the top of the UFO...
    don.begin_fill()
    don.left(90)
    don.forward(5)
    don.circle(13,180)
    don.forward(5)
    don.right(90)
    don.end_fill()

def spaceShip():
    x = random.randint(-400,400) #Creates random coordinates for the UFO to appear.
    y = random.randint(-300,300)
    don.penup()
    don.goto(x,y) #Moves the turtle to the random coordinates without drawing anything (penup and pendown).
    don.pendown()
    #Creates the 'movement' of the UFO through space.
    for i in range(100):
        window.tracer(0,50) #Stops the animation from flickering.
        don.clear()
        draw_Spaceship()
        window.update()
        don.forward(0.002)

window.tracer(0) #used to make the stars, plants and the milky way appear all at once.
for i in range(random.randint(50,150)): #Creates a random number of stars (between 50 and 150).
    star(horace,speed)
if bool(random.getrandbits(1)) == True: #Uses a true of false statement to decide if the milky way is drawn.
    milkyWay(horace)
for i in range(random.randint(0,3)): #Creates a random number of planets (between 0 and 3).
    planet(horace,speed)
if bool(random.getrandbits(1)) == True: #Uses a true of false statement to decide if the UFO is added.
    spaceShip()

turtle.done()
