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
        ret = 0
        if not data or len(data)==1:
            return ret
        copy = data
        self.quick_sort(copy)
        for i in copy:
            index = data.index(i)
            ret += index
            data.remove(i)
        return ret

    def quick_sort(self, data):
        if len(data) < 2:
            return data[:]
        left = self.quick_sort([i for i in data if i < data[0]])
        right = self.quick_sort([i for i in data if i > data[0]])
        return left + [data[0]] + right

