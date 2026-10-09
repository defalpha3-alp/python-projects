import random

target= random.randint(1,50)

while True:
    user_choice= input("Guess the number or Quit:")

    if(user_choice=="Quit"):
        break

    user_choice=int(user_choice)

    if(user_choice==target):
        print("Success: GUess is right !!")
        break

    elif(user_choice<target):
        print("Incorrect Guess: Number was too small.Guess Again:")

    else:
        print("Incorrect Guess: Number was too big. Guess Again:")
print("=====Game Over=====")
