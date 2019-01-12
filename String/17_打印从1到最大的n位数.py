# -*- coding:utf-8 -*-
class Solution:
    def print_max_n(self, n):
        # step1: 永远首先判断输入合法性
        if not n:
            return 0
        # step2: 最大的n 位数是10^n
        for i in range(1, 10**n):
            print(i)

s = Solution()
print(s.print_max_n(3))