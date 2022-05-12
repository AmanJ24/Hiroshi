
# new = 1
# num = [0]
# for i in range(34):
#     num.append(new)
#     new += num[i]
#     print(new)


# num = [0]
# n = 10
# a, b = 0, 1
# while n:
#     a, b = b, a + b
#     n -= 1
#     num.append(a)

# print(num)        

# num = 1634

# new = [int(i) ** 3 for i in str(num)]
# print(sum(new))


# def score(n): 

#     if n == 0:
#         return n
#     else:
#         list = ["0"]
#         for i in range(1, n):
#             list.append("|")
#             list.append(str(i))
#         return eval("".join(list))
# print(score(49))        

# count = []
# for i in range(103, 156):
#     if "5" not in str(i):
#         count.append(i)
# print(len(count))  

def replace_exclamation(s):
    # return ["!" if i in ['a', 'e', 'i', 'o', 'u'] else i for i in s.split()]
    return s.split()


print(replace_exclamation('aeious'))    