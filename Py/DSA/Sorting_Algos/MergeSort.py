#Divide the list into 2 parts and then choose the left one and then do it recursively until left with 1 item. then return it back and sort it, and keep moving up and doing same for all parts until get one single sorted list. 

def merge_sorted(arr1,arr2) :
    sorted_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j+= 1

    if i < len(arr1):
        sorted_arr.extend(arr1[i:])
    if j < len(arr2):
        sorted_arr.extend(arr2[j:])
        
    return sorted_arr


def MergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = MergeSort(arr[:middle])
        l2 = MergeSort(arr[middle:])
        return merge_sorted(l1, l2)

# xxxxxxxxxxxx Program Execution xxxxxxxxxxxx

# l = [8, 6, 2, 5, 1, 10, 7, 9, 4, 3]
# print(f"Sorted array: {divide_arr(l)}")