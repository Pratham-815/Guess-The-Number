import random

def check_answer(guess, answer):
    """Fuction to check user guess against actual answer"""

    if guess > answer:
        print("Too high!!!")
    elif guess < answer:
        print("Too low!!!")
    else:
        print(f"You got it!!! The answer was {answer}")

print("Welcome To The Number Guessing Game!!!")
print("I am thinking of a number between 1 to 100")

answer = random.randint(1,100)

guess = int(input("Make a guess: "))