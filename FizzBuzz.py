#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     13/05/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def start():
    multiple1 = int(input("What multiple would you like to be fizz?"))
    multiple2 = int(input("What multiple would you like to be buzz?"))
    gameLength = int(input("What number do you want the game to go to?"))
    for i in range(1,gameLength+1): #Checks every number up to and including gameLength.
        prime(i,multiple1,multiple2) #Goes to prime function.

def prime(i,multiple1,multiple2):
    if i > 1: #If the number is one, it doesn't do the loop, as we know that it's not a prime number.
        for l in range(2,i): #For the rest of the numbers....
            if i%l == 0: #If it can be divided with no remainders (is a multiple of another number(other than 1 and itself).
                fizzbuzz(i,multiple1,multiple2) #Goes to fizzbuzz function.
                break #stops the loop.
        else: #If it is a prime number...
            print("OOPS!") #prints OOPS! instead of the number.
    else: #If i is 1...
        fizzbuzz(i,multiple1,multiple2) #Goes to fizzbuzz function.


def fizzbuzz(i,multiple1,multiple2):
    if i%multiple1==0: #if the current number is a multiple of the first possibility...
            if i%multiple2==0: #checks if it is also a multiple of the second possibility.
                print("FizzBuzz") #prints fizzbuzz instead of the number.
            else: #if it's only a multiple of the first possibility...
                print("Fizz") #prints fizz instead of the number.
    elif i%multiple2==0: #if it's only a multiple of the second possbililty....
        print("Buzz") #prints buzz instead of the number.
    else: #if it's not a multiple of either of them...
        print(i) #Prints the number.


start() #Calls the first function.

