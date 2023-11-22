# amount = int(input("Enter an amount in cents: "))
# result_1 = amount / 100
# result_2 = amount / 25
# result_3 = amount / 10
# result_4 = amount / 5

# print(f"In dollar: {result_1}\nIn quarters: {result_2}\nIn dime: {result_3}\nIn nickel: {result_4}\nIn penny: {amount}")

# s = "test"
# # if type(len(s) / 2) == "float":
# #     print(s[len(s) // 2] + s[len(s) // 2 - 1])
# # else:
# #     print(s[len(s) // 2])


# print(s[len(s) // 2])
# print(s[len(s) // 2 - 1] + s[len(s) // 2])
cs = [ 3, 1, 2, 7, 1 ]
rs = [ 1, 8, 4, 5, 2 ]

black, num = 0, 0
total = sum(cs) * sum(rs)
# for i in rs:
#     if num % 2 == 0:
#         black += sum([i * j for j in cs if cs.index(j) % 2 == 1])
#         print(black)
#         print("***************************")
#     else:
#         black += sum([i * j for j in cs if cs.index(j) % 2 == 0])
#         print(black)
#         print("***************************")
# num += 1

print(cs)
print(cs[4])

print(cs.index(1))

print([1 * j for j in cs if cs.index(j) % 2 == 1])   