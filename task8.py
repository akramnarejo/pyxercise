import random
def choice(choice):
    """ This function takes in integer value and returns the equivalent string """
    if(choice == 1):
        return "Rock"
    elif(choice == 2):
        return "Paper"
    else:
        return "Scissors"

def determine(userChoice, computerChoice):
    """
        This function takes in two arguments userChoice and computerChoice,
        then determines and returns that who wins.
    """
    if(userChoice == "Rock" and computerChoice == "Paper"):
        return "computer"
    elif(userChoice == "Rock" and computerChoice == "Scissors"):
        return "user"
    elif(userChoice == "Paper" and computerChoice == "Rock"):
        return "user"
    elif(userChoice == "Paper" and computerChoice == "Scissors"):
        return "computer"
    elif(userChoice == "Scissors" and computerChoice == "Paper"):
        return "user"
    elif(userChoice == "Scissors" and computerChoice == "Rock"):
        return "computer"
    else:
        return "tie"

def play():
    """ Rock Paper Scissors is two person game, where eachone of them tosses the rock, paper or scissors.
        Followig are the rules:
        -Rock smashes the scissors.
        -Paper wraps the rock.
        -Scissors cut the paper.
    """
    print("-------Rock Paper Scissiors---------")
    print("1. Rock\n2. Paper\n3. Scissors")
    print("------------------------------------------------")
    rounds = int(input("Enter the number of rounds you want to play: "))
    print("------------------------------------------------")
    wins = []
    i=1
    while(i<=rounds):
        print(f'round {i}')
        print("-------")
        userChoice = int(input('Enter your choice(1,2,or 3): '))
        computerChoice = random.choice([1,2,3])
        print(f"You selected {choice(userChoice)}")
        print(f"computer selected {choice(computerChoice)}")
        winner = determine(choice(userChoice), choice(computerChoice))
        if(winner == "tie"):
            print("tie, nobody wins! \U0001F61F")
        else:
            print(f"{winner} wins! \U0001F602")
        wins.append(winner)
        print("------------------------------------------------")
        i+= 1
    userWins = 0
    computerWins = 0
    for win in wins:
        if(win == "user"):
            userWins += 1
        elif(win == "computer"):
            computerWins += 1
    if(rounds>1):
        if(userWins>computerWins):
            print("user wins! \U0001F602")
        elif(computerWins>userWins):
            print("computer wins!")
        else:
            print("tie, nobody wins! \U0001F61F")
    elif(rounds == 1):
        if(wins[0] == "tie"):
            print("tie, nobody wins! \U0001F61F")
        else:
            print(f"{wins[0]} wins! \U0001F602")

play()



