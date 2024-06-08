#Choose a pivot value, then move all the smaller values to the left and the larger ones to the right. Then choose the smaller list and apply the same logic again till you get a single value. Then move back up and you will have a sorted array. 

def QuickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for i in arr:
            if i > pivot:
                larger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                equal.append(i)
        return QuickSort(smaller) + equal + QuickSort(larger)



# l = [6, 4, 7, 2, 1, 5, 8, 10, 3, 9]
# print(QuickSort(l))