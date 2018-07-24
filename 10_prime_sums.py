def prime_sums(num):
    ret = 0
    for x in range(2, num):
        if isPrime(x):
           ret += x
    print(ret)

def isPrime(val):
    if val < 2: return "neither"
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            return False
    return True

prime_sums(2000000)