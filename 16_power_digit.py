def power_digit_sum(base, exp):
    exp_res = base ** exp
    nums = [int(i) for i in str(exp_res)]
    sum = 0
    for x in nums:
        sum += x
    # while exp_res > 0:
    #     sum += (int)(exp_res % 10)
    #     exp_res /= 10
    return sum

print(power_digit_sum(2, 1000))
