# student_heights = input("input a list of student heights: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_heights = 0
# for height in student_heights:
#     total_heights += height

# total_students = 0
# for students in student_heights:
#     total_students += 1

# average = round(total_heights / total_students)
# print(average)


def arr_adder(arr):
    new = ""
    for j in range(len(arr[0])):
        for i in arr:
            if i[j] != "":
                new += i[j]
            else:
                break    
        new += " "
    return new


output = [
            ['T','M','i','t','p','o','t','c'],
            ['h','i','s','h','o','f','h','e'],
            ['e','t','', 'e','w','', 'e','l'],
            ['', 'o','', '', 'e','', '', 'l'],
            ['', 'c','', '', 'r','', '', '' ],
            ['', 'h','', '', 'h','', '', '' ],
            ['', 'o','', '', 'o','', '', '' ],
            ['', 'n','', '', 'u','', '', '' ],
            ['', 'd','', '', 's','', '', '' ],
            ['', 'r','', '', 'e','', '', '' ],
            ['', 'i','', '', '', '', '', '' ],
            ['', 'a','', '', '', '', '', '' ]
        ]
# print(arr_adder(output))
print(" ".join(map("".join, zip(*output))))