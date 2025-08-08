import os
import random


green = "\033[42m"
yellow = "\033[43m"
rest = "\033[0m"

correct = random.choice(["SHARK" , "PLANE" , "ALARM", "ROBOT" , "EARTH", "PIZZA"])

for h in range(5):#5 chance
    guess = input("plz guess >> ").upper()
    for i in range(5):#check the word
        if guess[i] == correct[i]:
           print(f"{green}{guess[i]}{rest}" ,  end = " ")
        elif guess[i] in correct:
            print(f"{yellow}{guess[i]}{rest}" , end = " ")
        else:
            print(guess[i] , end=" ")
    print(" ")
       
    if guess == correct:
           print("YOU LOSE")
           exit()
           
print("YOU LOSE !")
print(f" the word is {correct}")
       
      