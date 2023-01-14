#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     28/05/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def start():
    convert_from = input("Do you have a binary, denary or hex number?").lower() #Asks for the type number the user wants converting.
    num = input("What is your number?") #Asks for the number.
    convert_to = input("What would you like to convert it to?").lower() #Asks for what they want it to be converted to.
    if convert_from == "binary":
        bina(num,convert_to) #If the first number is binary goes to bina function.
    elif convert_from == "denary":
        den(num,convert_to) #If the first number is denary goes to bina function.
    elif convert_from == "hex" or "hexadecimal":
        hexa(num,convert_to) #If the first number is hex goes to bina function.
    else:
        print("Sorry, I don't understand, please try again...") #If the input isn't understood prints this message.
        start() #Loops to ask again.

def bina(num,convert_to):
    if convert_to == "denary": #If converting to denary...
        binToDen(num) #Goes to function.
    else:
        binToHex(num) #Goes to function.


def den(num,convert_to):
    if convert_to == "binary": #If converting to binary...
        denToBin(num) #Goes to function.
    else:
        denToHex(num) #Goes to function.

def hexa(num,convert_to):
    if convert_to == "binary": #If converting to binary...
        hexToBin(num) #Goes to function.
    else:
        hexToDen(num) #Goes to function.


def binToDen(num):
    denary = int(num, 2) #Converts to denary.
    print(denary)

def denToBin(num):
    num = int(num)
    binary = "" #creates an empty string for the binary number.
    while num > 0:
        binary = str(num%2) + binary #converts to binary (adds the remainder to the binary string).
        num = num//2 #divides the number by 2.
    print(binary) #prints the final binary number.

def binToHex(num):
    temp = int(num, 2) #converts to denary.
    print(hex(int(temp))[2:].upper()) #prints the hex of the denary number.

def denToHex(num):
    print(hex(int(num))[2:].upper()) #prints the hex of the denary number.

def hexToBin(num):
    print(bin(int(num, 16))[2:]) #prints the bin of the hex number.

def hexToDen(num):
    denary = int(num, 16) #converts the hex number into denary.
    print(denary)

start() #Starts program