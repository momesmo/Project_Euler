import math


def is_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)
    n_half1 = n_str[:int(n_len/2)]
    n_half2 = n_str[math.ceil(n_len/2):]

    bin = "{0:b}".format(n)
    bin_len = len(bin)
    bin_half1 = bin[:int(bin_len / 2)]
    bin_half2 = bin[math.ceil(bin_len / 2):]
    print(n_half1, n_half2, bin_half1, bin_half2)

    if n_half1 == n_half2[::-1] and bin_half1 == bin_half2[::-1]:
        return True
    return False


def sum_2_base_palindromes(n):
    s = 0
    for i in range(0, n):
        if is_palindrome(i):
            s += i
    return s


print(sum_2_base_palindromes(1000000))
