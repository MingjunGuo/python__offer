# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        '''
        题目描述
        我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
        请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
        :param number:
        :return:
        '''
        # step1: 永远首先判断输入合法性
        if number <= 0:
            return 0
        if number < 2:
            return number
        else:
            a, b = 1, 2
            for i in range(2, number):
                a, b = b, a+b
            return b

s = Solution()
print(s.rectCover(0))
print(s.rectCover(1))
print(s.rectCover(2))
print(s.rectCover(3))
print(s.rectCover(10))