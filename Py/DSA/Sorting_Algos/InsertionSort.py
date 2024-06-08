#for each value check if every value before a value is smaller than it
#if not then replace and now again check with the new location of the value.

def insertion_sort(lst):
    for i in range(1, len(lst)):
        print('status: ' + str(lst))
        for j in range(i-1,-1,-1):
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

# lst = [12, 11, 13, 5, 6]
# print(insertion_sort(lst))