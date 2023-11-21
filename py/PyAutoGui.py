import pyautogui as pyy
import time



time.sleep(4)

for i in range(31):
    pyy.hotkey('ctrl', 'c')
    pyy.hotkey('alt', 'tab')
    pyy.hotkey('ctrl', 'v')
    pyy.hotkey('alt', 'tab')
    pyy.press('down')


    # pyy.press('enter')


# # count = 0
# # def deep_count(a):
# #     global count
# #     for i in a:
# #         count += 1
# #         if isinstance(i, list):
# #             deep_count(i)
# #     return count
        

# # print(deep_count([1,2,[3,4,[5]]]))









# import pandas as pd

# a = {
#     'one': [12,45,65,32,57,87],
#     'two': [34,65,12,98,67,34],
#     'three': [32,63,63,97,63,67],
#     'four': [65,12,98,67,34,12]
#     }


# df = pd.DataFrame(a, index = ['CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6'])
# '''
#        one  two  three  four
# CO1   12   34     32    65
# CO2   45   65     67    12
# CO3   65   12     45    98
# CO4   32   98     97    67
# CO5   57   67     35    34
# CO6   87   34     67    12
# '''




# print(df[['two','three']][df['two'] == 34])

# print(df[['two','four']][df['three'] == 63])
# import pandas as pd

# a = {
#     'year': [True, False, True, True],
#     'now': [1,2,3,4],
#     'yes': [5,6,7,8]
# }

# df = pd.DataFrame(a)

# print(df[df['year'] == True])






# import pandas as pd

# a = [1,2,3,4,5,None]
# b = [1,None,3,4,5,None]

# c = pd.Series(a)
# d = pd.Series(b)

# print(c+d)