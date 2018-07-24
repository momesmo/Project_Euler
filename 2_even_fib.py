def even_fib(limit) :
    temp = 0
    prev_fib = 1
    curr_fib = 2
    even_sum = 0
    while curr_fib < limit :
        if curr_fib%2 == 0:
            even_sum += curr_fib
        temp = curr_fib
        curr_fib = prev_fib + curr_fib
        prev_fib = temp

    print(even_sum)

even_fib(4000000)