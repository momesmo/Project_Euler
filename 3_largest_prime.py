def large_prime(prime):
    i = 2
    while i * i < prime:
        while prime % i == 0:
            prime /= i
        i += 1
    print(prime)

large_prime(600851475143)
