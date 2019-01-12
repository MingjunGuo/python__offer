def print_max(n):
    # step1: 永远首先检查输入合法性
    # step2: 最大的n 位数是10^-1
    for i in range(1, 10**n):
        print(i)