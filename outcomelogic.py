# This file contains a function that will take in user input then use to to decide who won
# Determining the winner will be based on a set of rules defined by the function. 
# Each outcome will be assigned a number. 0 = Computer win 1 = user win 2 = tie

# Function for determining Game Outcome
def deterRes(pchoice, cchoice):
    
    # Function starts off by determining if it is a tie or not
    if pchoice == cchoice:
        print("its a tie")
    else:
        match pchoice:
            case "Rock":
                print("user choose rock") #Debug
                if cchoice == "Paper":
                    print("You Lose")
                elif cchoice == "Scissors":
                    print("You Win")
            case "Paper":
                print("user choose paper") #Debug
                if cchoice == "Scissors":
                    print("You Lose")
                elif cchoice == "Rock": 
                    print("You Win")
            case "Scissors":
                print("user choose scissors")#Debug
                if cchoice == "Paper":
                    print("You Lose")
                elif cchoice == "Rock": 
                    print("You Win")
        print("not a tie")

    # DeBug Statements
    print(pchoice)
    print(cchoice)
    print("Debug")
