import random
while True:
    choices=["rock","paper","scissors"]
    player_choices=input("Enter you choice(rock,paper,scissors) : ")
    computer_choice=random.choice(choices)
    if player_choices not in choices:
        print("invalid choice choose again!")
        continue
    if player_choices == computer_choice:
         print("its a tie")
         continue
    elif player_choices=="rock" and computer_choice =="scissors" or\
         player_choices=="scissors" and computer_choice=="paper" or\
         player_choices=="paper" and computer_choice=="rock":
        print("you win")
        continue
    else:
        retry=(input("you lost you wonna try again(y,n)"))
        if retry is "y":
            continue
        else:
            print("thanks for playing!!")
            break       
