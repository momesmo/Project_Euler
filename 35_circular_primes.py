def circular_primes(n):
    lst = [n]
    s_n = str(n)
    for i in range(0, len(s_n)-1):
        new_s_n = s_n[1:] + s_n[:1]
        lst.append(int(new_s_n))
        s_n = new_s_n
    #print(lst)
    return lst


def is_prime(val):
    if val < 2: return "neither"
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            return False
    return True


def count_circular_primes(n):
    cnt = 0
    for i in range(2, n):
        chk_prime = 0
        cir_lst = circular_primes(i)
        #print(cir_lst)
        for x in cir_lst:
            if is_prime(x):
                chk_prime += 1
        #        print(chk_prime, len(cir_lst))
        if chk_prime == len(cir_lst):
            cnt += 1
        #print(cnt)
    return cnt

print(count_circular_primes(1000000))