import os
import random

correct = "SHARK"
guess = input("plz guess >> ")

for i in range(5):
   if guess[0] == correct[0]:
        print(f"{guess[0]}" ,  end = " ")
   elif guess[0] in correct:
        print(f"{guess[0]}" , end = " ")
   else:
         print(guess[0] , end=" ")