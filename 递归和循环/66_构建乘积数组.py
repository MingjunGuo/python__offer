# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        '''
        题目描述
        给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
        其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
        不能使用除法。
        :param A:
        :return:
        '''
        # step1: 首先判断输入合法性
        if not A:
            return []
        # step2: 看成主对角线为1， 下三角与上三角连乘
        mult = 1
        B = [1]*len(A)
        for i in range(len(A)):
            mult *= A[i-1] if i > 0 else mult
            for a in A[i+1:]:
                B[i] *= a
            B[i] = B[i] * mult
        return B

s = Solution()
A = [1, 3, 5, 7, 9]
print(s.multiply(A))
