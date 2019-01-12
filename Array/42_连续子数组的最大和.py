# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        '''
        题目描述
        HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
        今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
        当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
        并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
        给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
        :param array: 输入数组
        :return:返回最大连续子序列的和
        '''
        ret = float('-inf')  # 代表负无穷
        # Step1：永远先判断输入是否合法
        if not array:
            return ret
        # Step2: 目前和为负数时，则需要重新开始加和，如果为正数，则在此基础上继续进行加和
        current = 0
        for num in array:
            if current < 0:
                current = num
            else:
                current += num
            ret = max(ret, current)
        return ret

array = [-1,-3,4,-2,6,7,8,-10,-11]
array1 = []
array2 = [-1]
array3 = [1]
s = Solution()
print(s.FindGreatestSumOfSubArray(array))
print(s.FindGreatestSumOfSubArray(array1))
print(s.FindGreatestSumOfSubArray(array2))
print(s.FindGreatestSumOfSubArray(array3))