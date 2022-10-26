import random

def guess_the_number():
    random_number = random.randint(0, 5)

    while True:
        user_guess = int(input('What number am I? (Type in a number between 0 and 5): '))
        if user_guess > random_number:
            print("Too high. Try again!")
        
        elif user_guess < random_number:
            print("Too low. Try again!")
        
        else:
            print(f'You are correct!. The answer is {random_number}')
            print("*************************************************")
            print("*************************************************")
            print("*************************************************")
            print("Let's play again")
guess_the_number()