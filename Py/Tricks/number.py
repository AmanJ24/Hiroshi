#Getting all the divisors of a number

def is_perfect(n):
    return [x for x in range(1, n) if n/x==int(n/x)]

#--------------------------------------------------------

#For printing just the values of a list

data = [1, 2, 3, 4, 5, 6, 7]
print(data) #O/P--> [1, 2, 3, 4, 5, 6, 7]
print(*data) #O/P--> 1 2 3 4 5 6 7

#--------------------------------------------------------

#Days left in current year

import datetime; print((datetime.date(2022,12,31) - datetime.date.today()).days)

#----------------------------------------------------------

#converting every string to int in a list

list_1 = ["1", "2", "3", "4", "5", "6"]

now = list(map(int, list_1))

print(now) #O/P--> [1, 2, 3, 4, 5, 6]

#------------------------------------------------------------

#applying a function to every item in a list

nums = range(1, 100)

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

primes = filter(is_prime, nums)

print(list(primes))

#--------------------------------------------------------------

#assigning and printing the value at the same time using walrus operator

print(answer := 42)

#-------------------------------------------------------------

#explaining pointers

a = [1, 2, 3]
b = a
b[2] = 100
print(a) #O/P--> [1, 2, 100]

#-------------------------------------------------------------