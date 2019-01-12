# -*- coding:utf-8 -*-
class Solution:
    def find_integer(self, matrix, num):
        '''
        题目描述
        在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
        每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
        :param matrix: 二维数组
        :param num: 与之进行比较的数字
        :return: True / False
        '''
        # Step1: 永远先判断输入是否合法（matrix）
        if not matrix:
            return False

        # Step2: 从右上角开始进行比较， 大者向下，小者向左
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols-1
        while row <= rows-1 and col >= 0:
            if num == matrix[row][col]:
                return True
            elif num > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

s = Solution()
print(s.find_integer(array, 10))
print(s.find_integer(array, 14))
print(s.find_integer(array2, 10))
print(s.find_integer(array3, 'a'))
print(s.find_integer(array4, 81))


