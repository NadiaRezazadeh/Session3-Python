import random

while True:
   d = input("If you want to roll the dice, enter 's' if not enter 'q' :")
   if d == 's':
        dice = random.randint(1,6)
        if 1 <= dice <= 5:
            print("dice =" , dice)
        
        if dice == 6:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print("Hooray!dice = 6 , Bonus dice 1 =",dice1 , "Bonus dice 2 =",dice2 )

   if d == 'q':
        print("End")
        break       
                    