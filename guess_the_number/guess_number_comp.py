import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Congrats, you have guessed the number {random_number} correctly!")

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    print(f"Think of a number between 1 and {high}.")
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is the number {guess} too high (H), too low (L) or correct (C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer has guessed the number, {guess}, correctly!")

comp_guess(5000)
