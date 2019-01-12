# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        '''
        题目描述
        请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
        路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
        如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
        例如
        a b c e
        s f c s
        a d e e
        这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
        因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
        :param matrix:
        :param rows:
        :param cols:
        :param path:
        :return:
        '''
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        markMatrix = [0] * (rows * cols)
        pathlength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathlength, markMatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathlength, markMatrix):
        if len(path) == pathlength:
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col]==path[pathlength] and not markMatrix[row*cols+col]:
            pathlength += 1
            markMatrix[row * cols + col] = True
            hasPath = self.hasPathCore(matrix, rows, cols, row-1, col, path, pathlength, markMatrix) \
                      or self.hasPathCore(matrix, rows, cols, row+1, col, path, pathlength, markMatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col-1, path, pathlength, markMatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col+1, path, pathlength, markMatrix)
            if not hasPath:
                markMatrix[row * cols + col] = False
        return hasPath
