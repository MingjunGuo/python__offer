# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        '''
        题目描述
        输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
        例如，如果输入如下4 X 4矩阵：
        1 2 3 4
        5 6 7 8
        9 10 11 12
        13 14 15 16
        则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
        :param matrix:
        :return:
        '''
        # step1: 首先判断输入合法性
        if not matrix:
            return []
        # step2: 顺时针从外圈向里圈打印
        rows = len(matrix)-1
        cols = len(matrix[0])-1
        row, col = 0, 0
        ret = []
        while row <= rows and col <= cols:
            for y in range(col, cols+1):
                ret.append(matrix[row][y])
            for x in range(row+1, rows+1):
                ret.append(matrix[x][cols])
            if row < rows:
                for y in range(cols-1, col-1, -1):
                    ret.append(matrix[rows][y])
            if col < cols:
                for x in range(rows-1, row, -1):
                    ret.append(matrix[x][col])
            row += 1
            col += 1
            rows -= 1
            cols -= 1
        return ret

s = Solution()
matrix = [[1],[2],[3],[4],[5]]
print(s.printMatrix(matrix))