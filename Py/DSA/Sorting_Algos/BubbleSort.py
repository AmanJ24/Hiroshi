# Swap items adjacent and move on to the next until the last digit is at the correct place

def BubbleSort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    return arr



# lst = [6, 4, 1, 5, 2, 3, 8, 10, 7, 9]

# print(bubble_sort(lst))
