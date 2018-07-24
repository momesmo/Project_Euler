from math import gcd


def smallest_multiple(num):
    ret = 1
    for x in range(2, num+1):
        ret = ret * x / gcd(ret, x)
    print(ret)


smallest_multiple(20)
