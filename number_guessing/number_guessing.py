import random 
computer_guess=random.randint(1,10)
print("welcome to number guessing game")
while True:
 try:
  while True:
   player_guess=int(input("choose a number btw 1 to 10: "))
   if player_guess<1 or player_guess>10:
    print("dumb fuck its more than 10 u blind or sm,RETRY AGAIN!")
    continue
   if player_guess >computer_guess:
    print("too high")
   elif player_guess <computer_guess:
     print("too low")
   else:
    print("yay you won!")
    break
    
 except ValueError:
   print("invalid choose again")
   continue
 retry=input("do u want to continue?(y,n): ")
 if retry!="y":
     print("thank you for playing")
     break
   