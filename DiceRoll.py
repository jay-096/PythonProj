#Dice_roll_Simulator

import random as r

while True:
    print('''1. Roll the Dice      2.Exit''')
    user = int(input("what you want to do? \n"))
    if user == 1:
        number = r.randint(1,6)
        print("DIce shows = ", number)
    else:
        break