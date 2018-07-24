def first_prime(n):
    num_primes = 0
    prime_check = 1
    while num_primes < n:
        prime_check += 1
        if isPrime(prime_check):
            num_primes += 1
    print(prime_check)


def isPrime(val):
    if val < 2: return "neither"
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True


first_prime(10001)
