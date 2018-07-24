import math


def div_tri_num(num):
    factors = []
    tri_num = 0
    inc = 1
    while True:
        tri_num += inc
        inc += 1
        factors = factorize(tri_num)
        if len(factors) > num:
            return tri_num


def factorize(n):
    f = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            f.append(x)
            f.append(n/x)
    return f


print(div_tri_num(500))