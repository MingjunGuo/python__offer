# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        '''
        题目描述
        大家都知道斐波那契数列，现在要求输入一个整数n，
        请你输出斐波那契数列的第n项（从0开始，第0项为0）。
        n<=39
        :param n:
        :return:
        '''
        # step1: 首先判断输入合法性
        if n > 39:
            return 0
        # step2: 采用循环进行解决
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a


s = Solution()
print(s.Fibonacci(2))

