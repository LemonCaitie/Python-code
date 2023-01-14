#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     23/04/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getNumber():
    number = input("What is the credit card number?") #Asks for user input.
    number = ''.join(number.split()) #Gets rid of any spaces that have been typed by the user.
    if len(number) >= 13 and len(number) <= 19: #Checks the length of the number to see if could be valid.
        validate(number) #Goes to validate function.
    else:
        print("Invalid") #If it isn't a possible length prints invalid.

def validate(number):
    number = number[::-1] #Turns the string around so it is easier work from the 'right-hand'side later.
    number = [int(x) for x in number] #Makes number a list.
    double(number) #Goes to double function
    Sum = sum(number) #Adds the numbers of the list together.
    if Sum % 10 == 0: #If the total number ends in a 0...
        print("Valid")
    else:
        print("Invalid")

def double(number):
    for i in range(len(number)): #Does it for each number in the list.
        if i%2 != 0: #Makes sure only every other number is doubled
            number[i] = number[i]*2 #Doubles the number if so.
    twoFigures(number) #Goes to twoFigures function.

def twoFigures(number):
    for i in range(len(number)): #Does it for each number in the list.
        if number[i] > 9: #If the number is two digits...
            s = 0
            while number[i]: #Adds the digits together.
                s += number[i] % 10
                number[i] //= 10
            number[i] = s

getNumber()
