import time 
from random import choice
from string import ascii_lowercase as letters 

def binary_iter(n, arr):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return mid, f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1 
        else: 
            stop = mid - 1
    return None, f"{n} not found in the list."

def calculate_time(func, *arr):
    start = time.perf_counter()
    func(*arr)
    end = time.perf_counter()

    return f"{func.__name__}\t-> Elapsed time: {end - start:.5f}"


####### functions to generate lists of random emails #######

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def generate_emails(length_of_emails, list_of_domains, total_emails):
    emails = []
    for num in range(total_emails):
        emails.append(generate_name(length_of_emails) + "@" + get_domain(list_of_domains))
    return emails