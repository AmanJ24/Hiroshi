# --> REFACTORING A STRING TO BE PRINTED USING , 

# str1 = 100_000_000_000
# str2 = 100_0_0000_00

# total = str1 + str2
# print(f'{total:,}')



# --> TO INSERT A VALUE TO A LIST IN A LOGICAL MANNER USING ALGORITHM

# import bisect 

# num = [1, 3, 5, 9, 11, 13]
# val = 7


# # idx = bisect.bisect(num, val) --> shows the index to be inserted to
# bisect.insort(num, val)
# print(num)


# --> CLASSES BOILERPLATE INBUILT

# from dataclasses import dataclass

# @dataclass 
# class Player:
#     name: str
#     age: int

# person1 = Player("Aman", 25)
# person2 = Player("Aman", 25)
# print(person1)

# print(person1 == person2)


# --> PRINTING TWO LISTS CORRESPONDING TO EACH OTHER 

# a = [1, 2, 3, 4]
# b = ["one", "two", "three"]

# for val1, val2 in zip(a, b):
#     print(val1, val2)


# --> GOING THROUGH BOTH THE INDEX AND THE VALUE IN A LIST 

# data = [1, 2, -3, -4]

# for idx, val in enumerate(data):
#     if num < 0:
#         data[idx] = 0


# --> USED TO COUNT THE NUMBER OF ITEMS IN A LIST

# from collections import Counter

# my_list = [10, 10, 5, 2, 9, 9, 9]

# counter = Counter(my_list)

# print(counter) 
# print(counter[10])
# print(counter.most_common(1))



# --> MERGING TWO DICTIONARIES EXCLUDING THE COMMON ITEM

# x = {'a': 1, 'b': 2}
# y = {'b': 2, 'c': 3}

# z = x | y
# print(z)


#  --> REMOVING DUPLICATES MAINTAINING THE ORDER OF THE LIST

# duplicate_list = [12, 34, 34, 42, 34, 12, 75, 32, 42]

# print(list(dict.fromkeys(duplicate_list)))

#  --> RUNNING SYSTEM COMMANDS USING PYTHON

# import subprocess 
# subprocess.run(['ls', '-all'])

# import os
# os.system("ls -all")

# import subprocess 
# subprocess.Popen(["/usr/bin/git", "status"])


