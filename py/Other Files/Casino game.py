import random

logo = '''
  
   .oooooo.              .o.             .oooooo..o      ooooo      ooooo      ooo        .oooooo.        
  d8P'  `Y8b            .888.           d8P'    `Y8      `888'      `888b.     `8'       d8P'  `Y8b       
 888                   .8"888.          Y88bo.            888        8 `88b.    8       888      888      
 888                  .8' `888.          `"Y8888o.        888        8   `88b.  8       888      888      
 888                 .88ooo8888.             `"Y88b       888        8     `88b.8       888      888      
 `88b    ooo        .8'     `888.       oo     .d8P       888        8       `888       `88b    d88'      
  `Y8bood8P'       o88o     o8888o      8""88888P'       o888o      o8o        `8        `Y8bood8P'                                                                                                                 
'''

def game():
    game_on = True
    print(logo)

    name = input("Enter Player Name: ")
    deposit = int(input("Deposit Your Amount: $ "))
    
    while game_on:
        if deposit <= 0:
            print("Sorry, You are out of cash.")
            game_on = False
        else:    
            number = random.randint(1, 10)
            bet = int(input("How much would You like to bet?: $"))
            if bet <= deposit:
                deposit -= bet
                guess = int(input("Guess the number between 1 and 10: "))

                if guess == bet:
                    new = bet * 10
                    print(f"You won! and received ${new}.")
                    deposit += new
                    print(f"Amount left: {deposit}")
                else:
                    print("You lost!")
                    print(f"Amount left: ${deposit}")
            else:
                print("Sorry, The amount you entered exceeded your deposit.") 
                print(f"Amount left: ${deposit}")                   

wanna_play = input("Wanna play in our CASINO? Type 'y' or 'n': ")
if wanna_play == 'y' or wanna_play == 'Y':
    game()
elif wanna_play == 'n' or wanna_play == 'N':
    print("Ok, Fuck off!!!")
else:
    print("Idiot type something valid.")        