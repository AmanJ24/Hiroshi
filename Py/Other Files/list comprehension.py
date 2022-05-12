# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random 

# scores = {student: random.randint(1, 100) for student in names}

# passed = {student:score for (student, score) in scores if score >= 60}


# value = input("Enter the string: ")
# stipped = list(value)

def find_longest(string):
    spl = str.split(" ")
    longest = 0
    print(spl)
    # for i in spl:
    #     if len(i) > longest:
    #         longest = len(i)
    # return longest  

print(find_longest("This is a test subject"))    