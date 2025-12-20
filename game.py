## ROCK PAPER SCISSOR GAME
import random

entity = ["rock", "paper", "scissor"]
inx: int = random.randint(0, 2)

Rounds: int=int(input("Enter how many rounds you want to play?"))
for _ in range(0,Rounds):

    inx: int = random.randint(0, 2)
    PC: str = entity[inx]

    print("pls enter your choice.")

    USER = str(input("Enter any one-->(Rock,paper,scissor)")).lower()

    if PC==USER:
        print(f"The Match is a tie.you are {USER} pc is {PC}")

    elif(PC=="rock" or PC=="Rock") and (USER=="scissor" or USER=="Scissor"):
        print(f"You lost PC is {PC} you are {USER}")

    elif(PC=="Scissor" or PC=="scissor") and (USER=="rock" or USER=="Rock"):
        print(f"You Won , as you are {USER} VS {PC}")

    elif(PC=="paper" or PC=="Paper") and (USER=="rock" or USER=="Rock"):
        print(f"You lost {PC} vs {USER}")

    elif(PC=="rock" or PC=="Rock") and (USER=="Paper" or USER=="paper"):
        print(f"You Won {PC} vs {USER}")  

    elif(PC=="Scissor" or PC=="scissor") and (USER=="Paper" or USER=="paper"):
        print(f"You Lost { PC} vs {USER}")

    elif(PC=="Paper" or PC=="paper") and (USER=="scissor" or USER=="Scissor"):
        print("you won {PC} vs {USER}")

    else:
        print("pls enter valid string")       
