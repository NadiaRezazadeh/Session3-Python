import random

pc_number = random.randint(0,100)
t = 0

while True:
    user_number = int(input("Guess a number between 0 and 100 and enter it="))
   
    t += 1
    if pc_number == user_number :
        print("Yes , you won , you guessed ", t ,"time(s)")
        break 

    if pc_number > user_number :
         print("Guess a greater number")

    if pc_number < user_number :
         print("Guess a lower number")          
