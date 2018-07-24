def mult_3_5(num):
    sum = 0
    for x in range(1, num):
        if(x%3==0):
            sum += x
        elif(x%5==0):
            sum += x
    print(sum)

mult_3_5(1000)