#Keep a marker at each value and compare the marker with every value,
#replace the value if smaller but not the marker

def SelectionSort(lst):
    count = 0
    while count < len(lst):
        # print("Selection Sort status:" + str(lst))
        for i in range(count, len(lst)):
            if lst[count] > lst[i]:
                lst[count], lst[i] = lst[i], lst[count]
        count += 1

    return lst


# lst = [6, 4, 1, 5, 9 ,10 ,7, 8, 3, 2]
# print(selection_sort(lst))