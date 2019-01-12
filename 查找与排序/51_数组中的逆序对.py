# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        '''
        题目描述
        在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
        输入一个数组,求出这个数组中的逆序对的总数P。
        并将P对1000000007取模的结果输出。 即输出P%1000000007
        :param data:
        :return:
        '''
        if not data:
            return 0
        count = 0
        copy = [i for i in data]
        self.quick_sort(copy)
        for i in range(len(copy)):
            copy += data.index(copy[i])
            data.remove(copy[i])
        return count % 1000000007

    def quick_sort(self, tinput):
        if len(tinput) < 2:
            return tinput[:]
        left = self.quick_sort([i for i in tinput if i < tinput[0]])
        right = self.quick_sort([i for i in tinput if i > tinput[0]])
        return left + [tinput[0]] + right