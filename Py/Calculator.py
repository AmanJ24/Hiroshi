n1 = 1
n2 = 2

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

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbols in operators:
    print(symbols)
operation_symbol = input("Pick an operation from the operators above: ")
calculation = operators[operation_symbol]
answer = calculation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")