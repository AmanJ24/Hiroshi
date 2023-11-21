import os
os.system("cls")
    

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         )_________(
                       .-------------.
                      )_______________(

'''
print(logo)

auction = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid price?: $"))
    auction[name] = bid 
    repeat = input("If there are more bidders than type 'yes'. Otherwise 'no'. ") 
    if repeat == 'yes':
        os.system("cls")
    elif repeat == 'no':
        os.system("cls")
        should_continue = False
        i = 0
        for highest in auction:
            if auction[highest] > i:
                i = auction[highest]
        for thing in auction:
            if auction[thing] == i:
                print(f"The highest bidder is {thing} with a bid of {auction[thing]}.")        
    else:
        print("Invalid text.")


