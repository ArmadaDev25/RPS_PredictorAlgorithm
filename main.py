#File Imports
from choices import avalibleChoices
from outcomelogic import deterRes




# Variables
userChoices = [] # Holds the User's previous choices
logicRun = True
userEntry = None
algorEntry = None

# Program start Message
print('Lets Play Rock, Paper, Scissors')
input('Press a Key to Continue...')

# Algorithm will pick a random number that will determine which out of the 3 choices it will chose
# After the Algorithm sufficent data on what the user has previously chosen, it will begin to predict the users choice based on the data


# Main Program Loop
while logicRun:
    userEntry = input("Rock, Paper, or Scissors?")
    
    deterRes(userEntry, "me") # Debug
    logicRun = False 