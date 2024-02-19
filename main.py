import random

def check_answer(guess, answer):
    """Fuction to check user guess against actual answer"""

    if guess > answer:
        print("Too high!!!")
    elif guess < answer:
        print("Too low!!!")
    else:
        print(f"You got it!!! The answer was {answer}")


def set_difficulty():
    """Function to set difficulty of the game"""

    level = input("Choose difficulty level, type 'easy' or 'hard': ").lower()
    if level=='hard':
        return 5
    else:
        return 10
    

def game():
    print("Welcome To The Number Guessing Game!!!")
    print("I am thinking of a number between 1 to 100")

    answer = random.randint(1,100)

    lives = set_difficulty()
    print(f"You have {lives} attempts remaining to guess the number")

    guess = 0

    while guess != answer:
        
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)

game()