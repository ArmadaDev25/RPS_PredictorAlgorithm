# This file contains the logic that will drive the Algorithm an its decision making 

# Importd the avalibleChoices array from the choices file
# Used to determine which choice the Algorithm can pick
from choices import avalibleChoices 


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
    print("Debug from calculateChoiceChance Function") # Debug
    print(lengthOf) # Debug
    for choices in avalibleChoices:
        choiceChance.update({choices : userChoiceArray.count(choices)})
    print(choiceChance)

def mainLogicTree(userChoices):
    arraylength = len(userChoices) #Starts by getting the length of the userchoiceArray
    currentChoice = None
    print("These are the Users Preivious Choices according to the algorlogic.py file") # Debug
    print(userChoices) # Debug
    print('Length of the userChoices array: ', arraylength) # Debug
    # If 10 rounds have been played, the Algorithm with change how it chooses between Rock, Paper, and Scissors
    if arraylength >= 10:
        calculateChoiceChance(userChoices, arraylength)
        ## This Code is Placeholder Untill the Program is able to make Decisions based on what is predicts the user will choose
        currentChoice = makeRandomChoice()
        print('The Algorithm choose:' + currentChoice) # Debug
        return currentChoice
    else:
        currentChoice = makeRandomChoice()
        print('The Algorithm choose: ' + currentChoice) # Debug
        return currentChoice
    
  

    