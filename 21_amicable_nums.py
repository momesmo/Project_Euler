

def d(a):
    ret = 1
    for div in range(2, int(a/2)+1):
        if(a % div == 0):
            ret += div
            #print(div)
    return ret

def sum_amicables(num):
    sum = 0
    for x in range(1, num+1):
        if x == d(d(x)) and x != d(x):
            sum += x
    print(sum)

#print(d(220), d(d(220)))
sum_amicables(10000)