import random

rand_num = random.randint(1, 9)
guess = 0
no_of_guesses = 0

while guess != rand_num:
    guess = int(input("Guess a number between 1 and 9: "))
    no_of_guesses += 1
    if guess < rand_num:
        print("Try higher! ")
    elif guess > rand_num:
        print("Try lower!")
    else:
        print("Well done! Number of guesses required: " + str(no_of_guesses))