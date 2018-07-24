def find_sum_trunc_primes():
    num_trunc_primes = 0
    prime_check = 10
    both_prime = True
    while num_trunc_primes != 11 and both_prime:
        both_prime = True
        check_left = prime_check
        check_right = prime_check
        while check_left > 0:
            if not isPrime(check_left) or not isPrime(check_right):
                both_prime = False
            else:
                check_right /= 10
                check_left /= 10



def isPrime(val):
    if val < 2: return "neither"
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True