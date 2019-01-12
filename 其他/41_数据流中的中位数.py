# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ch = []

    def Insert(self, num):
        # write code here
        self.ch.append(num)
        self.ch.sort()

    def GetMedian(self, ch):
        # write code here
        '''
        数据流中的中位数
        题目描述
        如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
        如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
        :param ch:
        :return:
        '''
        if not self.ch:
            return None
        if len(self.ch) % 2 == 0:
            k = len(self.ch) / 2
            return (float(self.ch[k]) + float(self.ch[k - 1])) / float(2)
        else:
            k = (len(self.ch) + 1) / 2
            return float(self.ch[k - 1])
