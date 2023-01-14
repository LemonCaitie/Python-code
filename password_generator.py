#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     06/06/2020
# Copyright:   (c) caitl 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Random password generator

import random
import string

def makePassword():
    characters = string.ascii_letters + string.digits + string.punctuation #gets letters, numbers and punctuation.
    length = random.randint(12,20) #chooses a random length for the password (of a 'strong' length).
    password = (''.join(random.choice(characters) for i in range(length))) #choices random characters and adds them to the password string.
    print(password) #prints the password.
    file = open("passlist.txt","a") #opens a file.
    file.write(password+'\n') #adds the password to the file.
    file.close() #closes the file.

makePassword() #starts the function.