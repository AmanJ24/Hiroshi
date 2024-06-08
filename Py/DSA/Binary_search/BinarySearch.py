# Cut the list in half and check if the value is in the middle or left or right. then choose that section of the list and repeat the algo again till you are at the one value else return Not Found.


# -------------------------PROGRAM ------------------------------

# BINARY SEARCH USING ITERATION
def binary_iter(n, arr):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1 
        else: 
            stop = mid - 1
    return f"{n} not found in the list."

# BINARY SEARCH USING RECURSION
def binary_recur(n, arr, start, stop):
    mid = (start + stop) // 2
    if n == arr[mid]:
        return f"{n} found at index: {mid}"
    elif n > arr[mid]:
        return binary_recur(n, arr, mid+1, stop)
    else:
        return binary_recur(n, arr, start, mid-1)
    
    return f"{n} not found in the list."


# xxxxxxxxxxxxx PROGRAM EXECUTION xxxxxxxxxxxxxxxx

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = 2

print(binary_recur(value, lst, 0, len(lst)-1))