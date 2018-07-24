import math


def fact_dig_sum(num):
    sum = 0
    fact = [int(i) for i in str(math.factorial(num))]
    for x in fact:
        sum += x
    print(sum)


fact_dig_sum(100)
