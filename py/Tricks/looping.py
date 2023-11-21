def consecutive_sum(n:int) -> int:
    i = 1
    j = i+1
    total = i
    count = 0
    while True:
        if i < n:
            while total < n:
                total += j
                j += 1
            if total == n:
                count += 1
                i += 1
                total = i
                j = i+1
                continue
            else:
                i += 1
                total = i
                j = i+1
                continue
        else:
            return count





print(consecutive_sum(5))