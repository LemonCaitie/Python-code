#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     06/05/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pickle

class knowledge:
    pass

class Question(knowledge):
    def __init__(self, text, ifyes, ifno):
        self.text,self.ifyes,self.ifno = text,ifyes,ifno

    def play(self):
        if ask(self.text):
            self.ifyes = self.ifyes.play() #if the answer is yes, asks the right next question or gives an answer.
        else:
            self.ifno = self.ifno.play() #if the answer is no, asks the right next question or gives an answer.
        return self

class Answer(knowledge):
    def __init__(self,text):
        self.text = text

    def play(self):
        if ask("Are you thinking of a {}?".format(self.text)): #asks if it has guessed the right animal.
            print("I knew it!") #If it has, it prints the statement and ends the program.
            return self
        else: #if the instrument isn't correct...
            newInstrument = input("What instrument were you thinking of?") #asks the user for the correct answer.
            #asks the user for a question to distinguish between the correct answer and the instrument it suggested.
            newQuestion = input("What is a question to tell the difference between {} and {}?".format(self.text,newInstrument))
            #Finds out which instrument the question is true for, so it can format the question correctly, so it can ask in the next go.
            if ask("For {}, what should the answer be(yes or no)?".format(newInstrument)):
                return Question(newQuestion,Answer(newInstrument),self)
            else:
                return Question(newQuestion, self, Answer(newInstrument))

def ask(q):
    while True: #Continues this until there is a user input...
        ans = input(q+" ").lower() #Gets the user input.
        if ans == "yes": #If the answer is yes...
            return True #Return the boolean value True.
        elif ans == "no": #If the answer is no...
            return False #Returns the boolean value False.
        else: #If the input is not either of these, it asks for for the input to be yes or no.
            print("Please answer yes or no!")

try:
    file = open("instrument.kb","rb") #opens the file where the added questions are stored.
    kb = pickle.load(file)
    file.close()
except FileNotFoundError: #If the file hasn't been created yet (no new questions have been added), it fills in kb with the basic tree.
    kb = kb = Question("Is it a string instrument?",
        Question("Does it have four strings?", Answer("ukulele"), Answer("guitar")),
        Answer("flute"))


while True: #Creates a start loop, so the user can ask more than once down the tree.
    if not ask("Do you want to play?") :
        break
    kb = kb.play() #starts code

file = open("instrument.kb","wb") #opens the file for the added questions.
pickle.dump(kb,file) #Adds any questions that have been added this time round.
file.close() #Closes the file.
