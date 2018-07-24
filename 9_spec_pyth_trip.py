def pyth_trip(s):
    for i in range(0, 500):
        for j in range(0, 500):
            for k in range(0, 500):
                if i+j+k == s and i**2+j**2 == k**2:
                    return i*j*k

print(pyth_trip(1000))