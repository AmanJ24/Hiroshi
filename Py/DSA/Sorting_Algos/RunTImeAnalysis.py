import random 
import time
from BubbleSort import BubbleSort
from MergeSort import merge_sorted, MergeSort 
from SelectionSort import SelectionSort
from QuickSort import QuickSort

def calculate_time(arr, func):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()

    return f"{func.__name__}\t-> Elapsed time: {end - start:.5f}"

def analysis():
    sze = int(input("What size list do you want to create? "))
    rnge = int(input("What is the max value of the range? "))
    times = int(input("How many times do you want to run? "))

    lst = []

    for i in range(sze):
        lst.append(random.randint(10, rnge))

    for i in range(times):
        print(f"Run: {i+1}\n")
        print(calculate_time(lst, BubbleSort))
        print(calculate_time(lst, QuickSort))
        print(calculate_time(lst, MergeSort))
        print(calculate_time(lst, SelectionSort))
        print("-------------------------------------------")
    

analysis()

