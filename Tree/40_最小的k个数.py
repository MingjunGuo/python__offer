# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        '''
        题目描述
        输入n个整数，找出其中最小的K个数。
        例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
        :param tinput:
        :param k:
        :return:
        '''
        if len(tinput) < k:
            return []
        return self.quick_sort(tinput)[:k]

    def quick_sort(self, list):
        if len(list)<2:
            return list[:]
        left = self.quick_sort([i for i in list[1:] if i < list[0]])
        right = self.quick_sort([i for i in list[1:] if i > list[0]])
        return left + [list[0]] + right