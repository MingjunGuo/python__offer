# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        '''
        题目描述
        数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
        例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
        :param numbers:
        :return:
        '''
        if not numbers:
            return 0
        count = {}
        for num in numbers:
            count[num] = count[num] + 1 if count.get(num) else 1
            if count[num] > len(numbers)//2:
                return num
        return 0