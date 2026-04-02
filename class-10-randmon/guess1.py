import random

# computer picks one random number
comp_guess = random.randint(1, 50)
is_guess = True
while is_guess:
    user_guess = int(input("Enter Number b/w 1-50: "))

    if user_guess == comp_guess:
        print("Correct! You guessed the number.")
        is_guess = False

    elif user_guess > comp_guess:
        print("Too High")

    else:
        print("Too Low")