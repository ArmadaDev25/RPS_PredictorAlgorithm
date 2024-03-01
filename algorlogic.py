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

def calculateChoiceChance(userChoiceArray, lengthOf):
    print("CPU is now Predicting What the User Will Choose")# Debug to show when the algorithm starts to predict what the user will choose
    print(lengthOf) #debug

def mainLogicTree(userChoices):
    arraylength = len(userChoices) #Starts by getting the length of the userchoiceArray
    currentChoice = None
    print(arraylength) # Debug
    if arraylength >= 10:
        calculateChoiceChance(userChoices, arraylength)
        ## This Code is Placeholder Untill the Program is able to make Decisions based on what is predicts the user will choose
        currentchoice = makeRandomChoice()
        return currentChoice
    else:
        currentchoice = makeRandomChoice()
        return currentChoice
    


    