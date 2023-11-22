import os
import random
logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/   
'''
more_cards = True
def Game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    My_cards = []
    comp_cards = []
    a = random.choice(cards)
    b = random.choice(cards)
    c = random.choice(cards)
    d = random.choice(cards)
    My_cards.append(a)
    My_cards.append(b)
    comp_cards.append(c)
    comp_cards.append(d)
    print(f"Your cards: {My_cards}, current score: {sum(My_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")
    new_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while more_cards:
        if new_card == 'y' or new_card == 'Y':
            e = random.choice(cards)
            My_cards.append(e)
    print(f'''Your cards: {My_cards}, current score: {sum(My_cards)}, Computer's first card: {comp_cards[0]} 
    Your final hand: {My_cards}, final score: {sum(My_cards)}
    Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}''')
    if sum(My_cards) <=21 and sum(comp_cards) <= 21:
        if sum(My_cards) < sum(comp_cards):
            print("You went over.You lose!")
        elif sum(My_cards) > sum(comp_cards):
            print("You win!")
        elif sum(My_cards) == sum(comp_cards):
            print("Draw!")
    else:
        print("Your total went over 21. You lose!")

    again = input("Would You like to play again? Type 'y' to continue and 'n' to exit.: ")
    if again == 'y' or again == 'Y':
        Game()
    elif again == 'n' or again == 'N':
        print("Goodbye!")
    else:
        print("Invalid reply.")                    

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start == 'y' or start == 'Y':
    os.system("cls")
    Game()
elif start == 'n' or start == 'N':
    print("Goodbye!")
else:
    print("Invalid input.")        