# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        '''
        题目描述
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
        使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
        并保证奇数和奇数，偶数和偶数之间的相对位置不变。
        :param array: 输入数组
        :return: 重新排序后的数组
        '''
        # Step1: 永远先判断输入是否合法
        if len(array) <= 1:
            return array
        # Step2: 运用位与运算判断奇数/偶数
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right

array = [3,2,4,1,5,7,9,10]
s = Solution()
print(s.reOrderArray(array))