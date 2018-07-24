def largest_palin_product() :
    largest_palin = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            if str(x*y) == str(x*y)[::-1] and x*y > largest_palin:
                largest_palin = x*y
    print(largest_palin)

largest_palin_product()