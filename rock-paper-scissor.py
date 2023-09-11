import random
import os
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)

def txt():
    print("\t1. Rock\n\t2. Paper\n\t3. Scissor\n\t0. Exit\n")

clearConsole()
os.system("mode con lines=20 cols=50")

scorePlayer = 0
scoreBot = 0

while True:
    list = ["Rock", "Paper", "Scissor"]
    botChoice = random.choice(list)

    print("\n\t\tPlayer: " + str(scorePlayer) + "\tBot: " + str(scoreBot))
    txt()

    try:
        while True:
            playerChoiceTemp = int(input("\tPlayer choice: "))
            if playerChoiceTemp == 1:
                print("\n\tPlayer: Rock!")
            elif playerChoiceTemp == 2:
                print("\n\tPlayer: Paper!")
            elif playerChoiceTemp == 3:
                print("\n\tPlayer: Scissor!")
            elif playerChoiceTemp == 0:
                break
            else:
                print("\n\tInvalid choice try again!\n")
                continue
            break
    except ValueError:
        print("\n\tInvalid choice try again!\n")
        continue

    if playerChoiceTemp == 0:
        break
    else:
        print("\tBot: " + botChoice + "!\n\n")
        if (playerChoiceTemp == 1) and (botChoice == "Rock"):
            print("\t\t\tIt's a DRAW!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 1) and (botChoice == "Paper"):
            print("\t\t\tYou lose!")
            scoreBot += 1
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 1) and (botChoice == "Scissor"):
            scorePlayer += 1
            print("\t\t\tYou win!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 2) and (botChoice == "Rock"):
            scorePlayer += 1
            print("\t\t\tYou win!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 2) and (botChoice == "Paper"):
            print("\t\t\tIt's a DRAW!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 2) and (botChoice == "Scissor"):
            scoreBot += 1
            print("\t\t\tYou lose!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 3) and (botChoice == "Rock"):
            scoreBot += 1
            print("\t\t\tYou lose!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 3) and (botChoice == "Paper"):
            scorePlayer += 1
            print("\t\t\tYou win!")
            time.sleep(4)
            clearConsole()
            continue
        elif (playerChoiceTemp == 3) and (botChoice == "Scissor"):
            print("\t\t\tIt's a DRAW!")
            time.sleep(4)
            clearConsole()
            continue