def fib(num):
    f1 = 1
    f2 = 1
    nxt = 0
    str_check = ""
    i = 2
    while len(str_check) != num:
        i += 1
        nxt = f1 + f2
        str_check = str(nxt)
        f1 = f2
        f2 = nxt
    return i

print(fib(1000))