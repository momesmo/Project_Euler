def large_collatz_seq():
    longest_chain = 0
    longest_start = 0
    start = 1
    chain = []
    while start < 1000000:
        chain = make_collatz(start)
        if len(chain) > longest_chain:
            longest_chain = len(chain)
            longest_start = start
        start += 1
    print(longest_start)


def make_collatz(start):
    ret = [start]
    val = start
    while val != 1:
        if val % 2 == 0:
            val /= 2
        else:
            val = (3 * val) + 1
        ret.append(val)
    return ret


large_collatz_seq()
