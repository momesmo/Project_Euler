from math import factorial


def curious_factorials(n):
    nums = []
    num = n
    ret = 0
    for i in range(0, len(str(n))):
        nums.append(int(num%10))
        num /= 10
    for x in nums:
        ret += factorial(x)

    if n == ret:
        return ret
    else:
        return 0


def find_all():
    total = 0
    for i in range(2, 10000000):
        total += curious_factorials(i)
    print(total)


find_all()
