amount = int(input("Enter an amount in cents: "))
result_1 = amount / 100
result_2 = amount / 25
result_3 = amount / 10
result_4 = amount / 5

print(f"In dollar: {result_1}\nIn quarters: {result_2}\nIn dime: {result_3}\nIn nickel: {result_4}\nIn penny: {amount}")
