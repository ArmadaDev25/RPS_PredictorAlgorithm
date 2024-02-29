#File Imports
from choices import avalibleChoices
from outcomelogic import deterRes
from algorlogic import makeRandomChoice



# Variables
userChoices = [] # Holds the User's previous choices
logicRun = True
userEntry = None
algorEntry = None
roundsPlayed = 10

# Program start Message
print('Lets Play Rock, Paper, Scissors')
input('Press a Key to Continue...')

# Planning Notes
# Algorithm will pick a random number that will determine which out of the 3 choices it will chose
# After the Algorithm sufficent data on what the user has previously chosen, it will begin to predict the users choice based on the data


# Main Program Loop
while logicRun:
    isEntryValid = False
    userEntry = input("Rock, Paper, or Scissors? ")
    # Checks to Make sure the User input is valid
    while isEntryValid == False: 
        if userEntry in avalibleChoices: # Checks to see if what the user entered is in the avalibleChoices Array
            isEntryValid = True
        else:
            isEntryValid = False
            print("Please Enter a Valid Choice")
            userEntry = input("Rock, Paper, or Scissors?")


    # Records the User's choice to then be used by the Algorithm
    userChoices.append(userEntry)
    algorEntry = makeRandomChoice()
    deterRes(userEntry, algorEntry) # Sends the Algorithm's and the User's choices into the function that determines the outcome
    print(algorEntry) # Debug
    print(userEntry) # Debug
    print("This is the User's previous Choices")
    print(userChoices)
    userEntry = None
    # Asks if the player wants to play again after 10 rounds
    if roundsPlayed >= 10:
        playAgainChoice = input("Play Again? Type Y or N: ")
        match playAgainChoice:
            case "Y":
                logicRun = True
            case "N":
                logicRun = False 

    
    
    