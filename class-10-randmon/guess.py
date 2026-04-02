import random

is_guess=True
while is_guess:
    comp_guess=random.randint(1,50)
    user_guess=int(input("Enter Number b/w 1-50:::"))
    if user_guess==comp_guess:
        break
    elif user_guess>=25:
        print("Too High",": System Guess Value",comp_guess)

    else:
        print("Too Low",": System Guess Value",comp_guess)