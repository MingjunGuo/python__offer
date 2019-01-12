# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        '''
        题目描述
        输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
        如果有多对数字的和等于S，输出两个数的乘积最小的。
        :param array: 递增排序数组
        :param tsum:和
        :return:
        '''
        # Step1 : 永远先检查输入是否合法
        if not array:
            return []
        # Step2: 设置头尾两个指针， 如果和> S，尾指针-1， 如果和<S，头指针加1
        head, end = 0, len(array)-1
        while head < end:
            if tsum == array[head] + array[end]:
                return [array[head], array[end]]
            elif tsum > array[head] + array[end]:
                head += 1
            else:
                end -= 1
        return []

a = [1,2,3,4,5,6,7,8,9]
s = Solution()
print(s.FindNumbersWithSum(a, 18))
