# This file contains a function that will take in user input then use to to decide who won
# Determining the winner will be based on a set of rules defined by the function. 

# Function for determining Game Outcome
def deterRes(pchoice, cchoice):
    print("DEBUG: Values passed into deterRes Function")
    print('Player Choice: ', pchoice)
    print('Algorithm Choice: ', cchoice)
    
    
    # Function starts off by determining if it is a tie or not
    if pchoice == cchoice:
        print("Round Result: It's a tie")
    else:
        print("DEBUG: Continuing To Match Statment For Round Result") # Debug
        match pchoice:
            case "Rock":
                print("user choose rock") #Debug
                if cchoice == "Paper":
                    print("Round Result: You Lose")
                elif cchoice == "Scissors":
                    print("Round Result: You Win")
            case "Paper":
                print("user choose paper") #Debug
                if cchoice == "Scissors":
                    print("Round Result: You Lose")
                elif cchoice == "Rock": 
                    print("Round Result: You Win")
            case "Scissors":
                print("user choose scissors")#Debug
                if cchoice == "Paper":
                    print("Round Result: You Lose")
                elif cchoice == "Rock": 
                    print("Round Result: You Win")
        

    # DeBug Statements
    
