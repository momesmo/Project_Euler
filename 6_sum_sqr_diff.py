def sum_sqr_diff(num):
    lst = list(range(1, num+1))
    s = sum(lst)**2
    for x in lst:
        s -= x ** 2
    print(s)

sum_sqr_diff(100)