import random 

print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
''')

def easy_difficulty():
    number = random.randint(1, 100)
    should_continue = True
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    while should_continue:
        guess = int(input("Make a guess: "))
        if guess != number:
            attempts -= 1
            if attempts == 0:
                print("You lose.")
                should_continue = False
            elif guess > number:
                print("Too high.\nGuess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess < number:
                print("Too low.\nGuess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess == number:
            should_continue = False
            print(f"The number was {number}. You won!")

def hard_difficulty():
    number = random.randint(1, 100)
    should_continue = True
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    while should_continue:
        guess = int(input("Make a guess: "))
        if guess != number:
            attempts -= 1
            if attempts == 0:
                print("You lose.")
                should_continue = False
            elif guess > number:
                print("Too high.\nGuess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess < number:
                print("Too low.\nGuess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess == number:
            should_continue = False
            print(f"The number was {number}. You won!")  

                      
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    easy_difficulty()
elif difficulty == 'hard':
    hard_difficulty()
else:
    print("Invalid input.")