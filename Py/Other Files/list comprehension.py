# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random 

# scores = {student: random.randint(1, 100) for student in names}

# passed = {student:score for (student, score) in scores if score >= 60}


# value = input("Enter the string: ")
# stipped = list(value)

# def find_longest(string):
#     spl = str.split(" ")
#     longest = 0
#     print(spl)
#     # for i in spl:
#     #     if len(i) > longest:
#     #         longest = len(i)
#     # return longest  

# print(find_longest("This is a test subject"))    


# import pandas as pd

# one = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
# two = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
# three = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
# four = ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# data = pd.DataFrame([one, two, three, four])

# # print(data.iloc[:, 'a'::2])


# print(data.iloc[lambda x: x.index % 3 == 0])

# print(data.iloc[:, lambda data: [i for i in range(10) if i%3 != 0]])







# for i in range(1, len(one)+1, 3):
#     if i%3 != 0:
#         print(data.iloc[:, i-2:i])


# import matplotlib.pyplot as plt  
    
# plt.plot([1, 2, 3]) 
# plt.title('matplotlib.pyplot.plot() example 1')  
# plt.show()


import matplotlib.pyplot as plt

Country = [23, 39, 45, 46, 92]
gdp = [45000, 20000, 50000, 43000, 42000]

plt.pie(Country, gdp)
plt.xlabel('Country')
plt.ylabel('GDP')
plt.title('Here comes my diagram.')
plt.show()


# one = "Hello"
# two = "My Name"
# three = "is Aman"

# four = one + two + three
# five = " "
# print(five.join(four))
# print("Well: %s %s %s" % (one, two, three))


# def testit(a, b):
#     # return a*b if a/b > 0.5 else a+b
#     return a/b > 0.5
# print(testit(1,3))    

# def factorial(n):
#     a = 1
#     for i in range(1, n+1):
#         a *= i
#     return a
# print(factorial(3))    


# START:STOP:STEP
# 0: -1: 1