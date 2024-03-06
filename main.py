#File Imports
from choices import avalibleChoices
from outcomelogic import deterRes
from algorlogic import makeRandomChoice
from algorlogic import mainLogicTree



# Variables
userChoices = [] # Holds the User's previous choices
logicRun = True
userEntry = None
algorEntry = None
# This variable will hold the user's stats

userStats = {
    "Win" : 0,
    "Loss": 0,
    "Tie": 0

}

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
        try: 
            avalibleChoices.index(userEntry)
        except ValueError:
            input("Please Input a Valid Choice")
        else:
            isEntryValid = True

    userChoices.append(userEntry) # Records the User's choice to then be used by the Algorithm
    algorEntry = mainLogicTree(userChoices)
    roundOutcome = deterRes(userEntry, algorEntry) # Sends the Algorithm's and the User's choices into the function that determines the outcome. Then stores the returned outcome to be displayed to the player
    print("Debug From main.py") # Debug
    print(algorEntry) # Debug
    print(userEntry) # Debug
    print("This is the User's previous Choices - According to main.py File") # Debug
    print(userChoices) # Debug

    #Print Statment that shows the Player the Results of the round
    print("#################", "\n     RESULTS", '\n' + roundOutcome, "\n#################")
    


    userEntry = None #Resets the users choice for the next round
    # Asks if the player wants to play again after 10 rounds
    # Determines if 10 rounds have been played by checking the length of the UserChoices Array
    if len(userChoices) >= 10:
        playAgainChoice = input("Play Again? Type Y or N: ")
        match playAgainChoice:
            case "Y":
                logicRun = True
            case "N":
                logicRun = False 

    
    
    