# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        result = float('-inf')
        if not array:
            return result
        current = 0
        for i in array:
            if current >= 0:
                current += i
            else:
                current = i
            result = max(result, current)
        return result