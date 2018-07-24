def distinct_powers(a, b):
    lst = []
    for x in range(2, a+1):
        for y in range(2, b+1):
            lst.append(x**y)
    return len(set(lst))


print(distinct_powers(1000, 1000))