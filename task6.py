import os


os.system("clear")

#the word
correct = "SHARK"

guess = input("plz guess >> ").upper()

if guess[0] == correct[0]:
    print(f"{guess[0]}" , end =" ")
else:
    print("wrong answer")