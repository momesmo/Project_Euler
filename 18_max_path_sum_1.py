def max_path_sum():
    arr = []
    add_arr = []
    for line in reversed(list(open("max_path_sum.txt"))): # p067_triangle.txt
        barr = [int(n) for n in line.split()]
        arr.append(barr)
    for i in range(len(arr) - 1):
        print('++++++')
        curr_row, nxt_row = arr[i], arr[i + 1]
        add_arr = []
        for j in range(len(curr_row) - 1):
            curr_ele, nxt_ele, top_ele = curr_row[j], curr_row[j + 1], nxt_row[j]
            if curr_ele > nxt_ele:
                add_arr.append(curr_ele + top_ele)
            else:
                add_arr.append(nxt_ele + top_ele)
            #print(add_arr[j])
        arr[i + 1] = add_arr
        print('updated arr', arr[i + 1])
        print('=======')

max_path_sum()