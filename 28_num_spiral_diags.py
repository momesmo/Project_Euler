def spiral_diag_sum(n):
    nums = [i for i in range(1, n*n+1)]
    skip_amnt = 2
    skip_times = 0
    s = 0
    i = 0
    while i < len(nums):
        s += nums[i]
        print("i=", i, "s=", s)
        if skip_times % 4 == 0 and skip_times != 0:
            skip_amnt += 2
        i += skip_amnt
        skip_times += 1
    return s

print("Final", spiral_diag_sum(1001))