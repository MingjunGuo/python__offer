# -*- coding:utf-8 -*-
class Solution:
    def get_more_half_num(self, array):
        '''
        题目描述
        数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
        例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
        :param array: 输入的数组
        :return: 超过数组长度一半的数字
        '''
        # Step1: 永远先判断输入的合法性
        if array == None or len(array)<=0:
            return 0
        # Step2: 使用dict 进行解决
        hashes = dict()
        length = len(array)
        for n in array:
            hashes[n] = hashes[n]+1 if hashes.get(n) else 1
            if hashes[n] > length / 2:
                return n
        return 0

array = [2,2,2,4]
array1 = [1,2,2,1]
array2 = []
array3 = [1]
s = Solution()
print(s.get_more_half_num(array))
print(s.get_more_half_num(array1))
print(s.get_more_half_num(array2))
print(s.get_more_half_num(array3))

