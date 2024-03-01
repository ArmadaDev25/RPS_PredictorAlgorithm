# This file contains a function that will take in user input then use to to decide who won
# Determining the winner will be based on a set of rules defined by the function. 

# Function for determining Game Outcome
def deterRes(pchoice, cchoice):
    print("DEBUG: Values passed into deterRes Function")
    print('Player Choice: ', pchoice)
    print('Algorithm Choice: ', cchoice)
    
    outcomeResult = None # Variable that will hold the outcome result. Funtion will use this variable to pass data to the main.py file
    # Function starts off by determining if it is a tie or not
    if pchoice == cchoice:
        print("Round Result: It's a tie") #Debug
        outcomeResult = "Tie"
        return outcomeResult
    else:
        print("DEBUG: Continuing To Match Statment For Round Result") # Debug
        match pchoice:
            case "Rock":
                print("user choose rock") #Debug
                if cchoice == "Paper":
                    print("Round Result: You Lose") #Debug
                    outcomeResult = "You Lose"
                    return outcomeResult
                elif cchoice == "Scissors":
                    print("Round Result: You Win") #Debug
                    outcomeResult = "You Win"
                    return outcomeResult
            case "Paper":
                print("user choose paper") #Debug
                if cchoice == "Scissors":
                    print("Round Result: You Lose") #Debug
                    outcomeResult = "You Lose"
                    return outcomeResult
                elif cchoice == "Rock": 
                    print("Round Result: You Win") #Debug
                    outcomeResult = "You Win"
                    return outcomeResult
            case "Scissors":
                print("user choose scissors") #Debug
                if cchoice == "Paper":
                    print("Round Result: You Lose") #Debug
                    outcomeResult = "You Lose"
                    return outcomeResult
                elif cchoice == "Rock": 
                    print("Round Result: You Win") #Debug
                    outcomeResult = "You Win"
                    return outcomeResult
        

    # DeBug Statements
    
