#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caitl
#
# Created:     26/04/2021
# Copyright:   (c) caitl 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

class Map():
    grid = []
    neighbours = []
    def __init__(self,columns,rows):
        for i in range(columns): # for each column...
            self.grid.append([Cell.cellGenerate() for j in range(rows)]) #creates a empty list of a given length

        for i in range(columns): #for each column...
            self.neighbours.append([0 for j in range(rows)]) #shows that each cell has no neighbours to start

        Map.display(self.grid,self.neighbours) #goes to the display method

    def extinction(grid,neighbours):
    #check if whole grid is empty
        ex = True #variable for extinction value - it's assumed it's extinct
        for i in range(len(grid)): #for each for each row
            for j in range(len(grid[i])): #for each 'cell'
                if grid[i][j] == "f": #if there us a cell that is full/'f'
                    ex = False #exctinction is false
        if ex == False: #if extinction is false...
            Map.check(grid,neighbours) #goes to check method
        else:
            print("The simulation is extinct.") #gives extinction message to user

    def display(grid,neighbours):
        for i in range(len(grid)): #for the whole grid...
            print(grid[i], "\n") #prints a line of the grid on one line
        print("\n") #gives an empty line between grids
        Map.extinction(grid,neighbours) #goes to the method exctinction

    def check(grid,neighbours):
        for i in range(len(grid)): #for each for each row
            for j in range(len(grid[i])): #for each 'cell'
                count = 0
                #check the surrounding cells
                if  i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                    for h in range(j-2, j+1):
                        for l in range(i-2, i+1):
                            if grid[h][l] == "f":
                                count += 1
                neighbours[i][j] = count #puts the number of neighbours in the list
        Map.reloadMap(grid,neighbours) #goes to method reloadMap

    def reloadMap(grid,neighbours):
        for i in range(len(grid)): #for each for each row
            for j in range(len(grid[i])): #for each 'cell'
                grid[i][j] = Cell.reload(grid[i][j],neighbours[i][j]) #goes to the method reload in the class Cell
        Map.display(grid,neighbours) #goes to the method display

class Cell():

    def cellGenerate():
        ch = random.choice([True,False]) #picks true of false
        if ch == True:
            return "f" #gives the user a full/'f' cell
        else:
            return "e" #gives the user an empty/'e' cell

    def reload(currentState,neighbours):
        if neighbours == 3: #if the cell has three neighbours exactly...
            return "f" #the cell is full
        if neighbours == 2 and currentState == "f": #if the cell has two neighbours and is already full...
            return "f" #the cell is full
        else:
            return "e" #the cell is empty

Map(int(input("How many columns do you want?")),int(input("How many rows do you want?"))) #calls the Map class, starting the code.
