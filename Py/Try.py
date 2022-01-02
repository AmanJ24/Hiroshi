print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
step_1 = input("Decide your way = left or right: ").lower()
if(step_1 == "left"):
    print("You now have reached a river.")
    step_2 = input("Swim or wait: ").lower()
    if(step_2 == "wait"):
        print("Now you have come across the river via boat.")
        step_3 = input("Which door: red, yellow or blue: ").lower()
        if(step_3 == "yellow"):
            print("You Win!")
        else:
            print("You have chosen the wrong room. Game Over.")    
    else:
        print("The sharks ate you. Game Over.")
else:
    new = input("You really didn't make a good choice but You are gonna get one more chance. Choose East or West: ")

if(new == 'West'):
    step_4 = input("You have now come across a way with 3 different ways.\nType Plain for the fine road\nType Grass for the leafy road\nType Rocky for the stony road: ")
    if(step_4 == 'Plain'):
        step_5 = input("You are now in front of a cave. Press Enter to enter the cave or press Wait to wait outside the cave:")
        if(step_5 == 'Wait'):
            step_6 = input("You waited for a long time. Nothing really happened. Press Enter to enter the cave: ")
            if(step_6 == 'Enter'):
                step_7 = input("OMG!!! There is a Grizzly Bear in front of you. You must act fast, type quickly - Either Attack the Bear\nRun from there Or Stay still: ")
                if(step_7 == 'Stay'):
                    print("Congratulations, The bear has left the cave and You found a traeasure inside the cave. You Won!")
                elif(step_7 == "Attack"):
                    print("What were you thinking, Its a bear and You can't fight a bear. You lost.")
                elif(step_7 == "Run"):
                    Print("Bears can run too and even faster than you. Game lost.")
                else:
                    print("Invalid step")
            else:
                print("Invalid step")
        elif(step_5 == "Enter"):    
            step_7 = input("OMG!!! There is a Grizzly Bear in front of you. You must act fast, type quickly - Either Attack the Bear\nRun from there Or Stay still: ")
            if(step_7 == 'Stay'):
                print("Congratulations, The bear has left the cave and You found a traeasure inside the cave. You Won!")
            elif(step_7 == "Attack"):
                print("What were you thinking, Its a bear and You can't fight a bear. You lost.")
            elif(step_7 == "Run"):
                Print("Bears can run too and even faster than you. Game lost.")
            else:
                print("Invalid step")
        else:
            print("Invalid step")
    elif(step_4 == "Grass"):
        step_8 = input("OHHH! There jumped a Leapord in front of you. Type Attact to fight\nType Run to run from it: ") 
        if(step_8 == "Run"):
            print("You surely can't over-run a Leapord. Game over!")
        elif(step_8 == "Attact"):
            print("It's a leapord, What were You thinking. You died, Game over!")
        else:
            print("Invalid step")
    elif(step_4 == "Rocky"):
        Step_9 = input("You now come across a Mountain. You must Cross it: ")
        if(step_9 == "Cross"):
            print("Climbing wasn't really a great option. Game over!") 
        else:
            print("Invalid step") 
    else:
        print("Invalid step")
elif(new == "East"):
    step_10 = input("You now came across a countryside where there are many fields. Wanna go through them (y/n): ")
    if(step_10 == "y"):
        print("That was a trap. You fell into a hole. Game over!")
    elif(step_10 == "n"): 
        print("There came a few muggers who never let anyone alive. Game over!")
    else:
        print("Invalid step")
else:
    print("Invalid step")                                         
















