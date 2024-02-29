# This file contains the logic that will drive the Algorithm an its decision making 

# Importd the avalibleChoices array from the choices file
# Used to determine which choice the Algorithm picked
from choices import avalibleChoices 
# Imported the userChoices array from main


# Python Imports
import random

# Variables
choiceChance = {
    "Rock" : 0,
    "Paper": 0,
    "Scissors": 0

}

def makeRandomChoice():
    currentChoice = None
    # Will generate a number between 0 and 2 which corresponds to an index in the avalibleChoices array
    currentChoice = avalibleChoices[random.randint(0,2)]
    print(currentChoice)
    return currentChoice

def calculateChoiceChance(userChoiceArray):
    arraylength = len(userChoiceArray) #Starts by getting the length of the userchoiceArray
    print(arraylength) #debug

def mainLogicTree(userChoices):
    calculateChoiceChance(userChoices)