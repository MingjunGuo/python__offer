# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        '''
        题目描述
        输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
        :param n:
        :return:
        '''
        if n < 0:
            n = n & 0xffffffff
        ret = 0
        while n:
            ret += 1
            n = (n-1) & n
        return ret