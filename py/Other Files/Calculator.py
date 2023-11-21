n1 = 1
n2 = 2
import os
Logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
}
def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for symbols in operators:
        print(symbols)

    conti = True

    while conti:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation = operators[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


    
        ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if ask == 'y':
            num1 = answer
        elif ask == 'n':
            conti = False
            os.system('cls')
            calculator()
        else:
            print("Invalid input.")    

calculator()            