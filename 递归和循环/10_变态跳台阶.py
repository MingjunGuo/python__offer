# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        '''
        题目描述
        一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
        求该青蛙跳上一个n级的台阶总共有多少种跳法。
        :param number:
        :return:
        '''
        # step1: 永远首先检查输入合法性
        # step2: 变态跳台阶是2的次方
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

s = Solution()
print(s.jumpFloorII(3))