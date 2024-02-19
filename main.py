import random

def check_answer(guess, answer, turns):
    """Fuction to check user guess against actual answer"""

    if guess > answer:
        print("Too high!!!")
        return turns-1
    elif guess < answer:
        print("Too low!!!")
        return turns-1
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

    from art import logo
    print(logo)

    print("Welcome To The Number Guessing Game!!!")
    print("I am thinking of a number between 1 to 100")

    answer = random.randint(1,100)

    lives = set_difficulty()

    guess = 0

    while guess != answer:
        
        print(f"You have {lives} attempts remaining to guess the number")   
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, answer, lives)

game()