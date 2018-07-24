import time
import math
#from Euler import d


def divs(num):
    yield 1
    large = int(math.sqrt(num))
    if large * large == num:
        yield large
    else:
        large += 1
    for i in range(2, large):
        if num % i == 0:
            yield i
            yield num / i


def is_abundant(num):
    if num < 12:
        return False
    return sum(divs(num)) > num


def is_abundant_sum(num):
    a_lst = [x for x in range(1, num + 1) if not is_abundant(x)]
    a_set = set(a_lst)
    for i in a_lst:
        if i > num:
            return False
        if (num - i) in a_set:
            return True
    return False


t_start = time.time()

print(sum(x for x in range(1, 10000) if not is_abundant_sum(x)))

t_end = time.time()
print("It took:", t_end - t_start)
