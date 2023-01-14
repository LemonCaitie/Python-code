#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     21/04/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#List for alphanumeric and morse.
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morse = ["|",".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def alphToMorse(alphabet,morse):
    cypherText = "" #Creates the variable for the final morse message.
    plainText = str(input("What would you like in morse code?")) #Asks for user input and saves it.
    plainText.lower()#Makes the string all lower case so it can be found in the alphabet string.
    for i in range(len(plainText)): #Goes through the whole string of input.
        for c in range(len(alphabet)): #Goes through the alphabet list until...
            if plainText[i] == alphabet[c]: #The letter in the string matches the letter in the alphabet list.
                cypherText += " " + morse[c] #Finds the morse code for that letter and adds it to the final string.
    print(cypherText) #Prints the final message.

def morseToAlph(alphabet,morse):
    cypherText = "" #Creates the variable for the final alphanumeric message.
    plainText = str(input("What morse code would you like converting?")).split() #Splits the input into the morse 'letters' so it can be converted.
    for i in range(len(plainText)): #Goes through the whole string of input.
        for c in range(len(morse)): #Goes through the morse list until...
            if (plainText[i] != " ") and (plainText[i] == morse[c]): #if the morse from the string matches morse from the list...
                cypherText += alphabet[c] #It finds the alphanumeric value and adds it to the string.
    print(cypherText) #Prints the final message.

alphToMorse(alphabet,morse)
morseToAlph(alphabet,morse)