# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        '''
        题目描述
        在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
        输入一个数组,求出这个数组中的逆序对的总数P。
        并将P对1000000007取模的结果输出。 即输出P%1000000007
        :param data: 输入数组
        :return:
        '''
        # Step1: 永远先判断输入是否合法
        if not data:
            return 0
        # Step2: 复制后的数据进行排序，与原位置的差值即表示有多少比它大的数在它前面
        count = 0
        copy = [i for i in data]
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007

a = [1,2,3,4,5,6,7,0]
b = [1,2,4,3,5,6,7,0]
s = Solution()
print(s.InversePairs(a))
print(s.InversePairs(b))