# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][3])
      


# def hydrate(string): 
#     new = sum([int(i) for i in string.split(" ") if i.isdigit() == True])
#     return new

# print(hydrate('1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer'))

# n = 123456
# odd = int("".join([i for i in str(n) if int(i) % 2 == 0]))
# print(type(odd))

# x = 'abc'
# num = "".join([str(ord(i)) for i in x])
# new = "".join([str(i) if i != '7' else '1' for i in num])    

# print(int(num) - int(new))


# def row_sum_odd_numbers(n):
#     return [i for i in range(1, sum([i for i in range(1,n+1)] * 2)) if i % 2 == 1]

# print(row_sum_odd_numbers(2))    

# def func(string):
#     return string
# print("abc" is "abc")
# print("abc" is func("abcd"[:-1]))    

# s = "abracadabrra"
# words = [i for i in s]

# first = []
# num = 0
# for i in words:
#     if num % 2 == 0:
#         first.append(i.upper())
#     else:
#         first.append(i.lower())  
#     num += 1      
# print(first)

# print(words)

# import pandas as pd 
# info = {'Students': ['Aman', "Beauty", "Golden", "Happiness", "Rikita"], 'Marks': [10,20,30,40,50]}
# data = pd.DataFrame(info)

# data.at[2, 'Students'] = "Love"

# data.iloc[3, 1] = "Lover"
# print(data)

# n = 73567465519280238573

# count = 1
# while n > 1:
#     if n%2 == 0:
#         n /= 2
#     elif n%2 != 0:
#         n = (n*3) + 1
#     count += 1
#     print(count)

#73567465519280238573  


def bubblesort_once(m):
    l = [i for i in m if i != max(m)]
    new = [0]
    for i in range(len(m)-2): 
        new.append(max(l[i], l[i+1]))
        new.append(min(l[i], l[i+1]))
    new.append(max(m))
    return new[1::2]

print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))    