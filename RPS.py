import random

user_choice=int(input("Enter your choice: 0. Rock  1. Paper  2. Scissor \n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid Number, TRy Again!")
else:
    comp_choice=random.randint(0,2)
    print("Comps choice= ", comp_choice)
# order of conditions really matter
    if comp_choice == user_choice:
        print("its a draw")
    elif user_choice == 0 and comp_choice == 2:
        print("you win")
    elif comp_choice > user_choice:
        print("you lose")
    elif comp_choice == 0 and user_choice == 2:
        print("you lose")
    elif user_choice > comp_choice:
        print("you win")



