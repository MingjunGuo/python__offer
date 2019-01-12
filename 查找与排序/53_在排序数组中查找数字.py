# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        '''
        题目描述
        在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
        :param target:
        :param array:
        :return:
        '''
        if not array:
            return None
        row = 0
        col = len(array[0])-1
        while row <= len(array)-1 and col>=0:
            if array[row][col] == target:
                return True
            if array[row][col] < target:
                row += 1
            else:
                col -= 1
        return False