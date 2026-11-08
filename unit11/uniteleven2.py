import os
import random

the_sectret_number = random.randint(1, 10)

while True:
    guess = int(input("Please guess a number between 1 and 10 \n"))
    
    if guess == the_sectret_number:
        print("Congratulations ! you guessed the number !")
        break
    else:
        input("wrong guess , press Enter to try again")
        
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
