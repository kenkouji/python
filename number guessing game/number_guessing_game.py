import random
computer_choice=random.randint(1,100)
while True:
  try:
     player_choice=int(input("enter a number"))

     if player_choice > computer_choice:
        print("the guessed number is high")
     elif player_choice < computer_choice:
        print("the guessed number is low")
     else:
        print("yayy you guessed the number right")
        break 
  except ValueError: 
     print("invlaid choice choose again")