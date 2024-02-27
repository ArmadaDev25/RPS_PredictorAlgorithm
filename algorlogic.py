# This file contains the logic that will drive the Algorithm an its decision making 

# Importd the avalibleChoices array from the choices file
# Used to determine which choice the Algorithm picked
from choices import avalibleChoices 

# Python Imports
import random

def makeRandomChoice():
    currentChoice = None
    # Will generate a number between 0 and 2 which corresponds to an index in the avalibleChoices array
    currentChoice = avalibleChoices[random.randint(0,2)]
    print(currentChoice)
    return currentChoice

