def irrational_frac(n):
    fraction = ""
    cnt = 1
    while len(fraction) < n:
        fraction += str(cnt)
        cnt += 1
        #print(fraction)
    return fraction


def champerownes_constant():
    dec_frac = irrational_frac(1000000)
    print(dec_frac)
    print(int(dec_frac[1000000]) , int(dec_frac[100000]) , int(dec_frac[10000]) , int(dec_frac[1000]) , int(dec_frac[100]) , int(dec_frac[10]) , int(dec_frac[1]))
    return int(dec_frac[1000000]) * int(dec_frac[100000]) * int(dec_frac[10000]) * int(dec_frac[1000]) * int(dec_frac[100]) * int(dec_frac[10]) * int(dec_frac[1])


print(champerownes_constant())
