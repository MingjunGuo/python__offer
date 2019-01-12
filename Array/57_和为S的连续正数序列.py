# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        '''
        题目描述
        小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
        但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
        没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
        现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
        :param tsum:
        :return:
        '''
        # Step1: 永远先判断输入是否合法
        if not tsum:
            return []
        # Step2: 使用两个指针指向1，2， 和比tsum小， 大指针后移， 和比tusm 大， 小指针后移
        a,b = 1,2
        ret = []
        while a < tsum/2 + 1:
            if tsum == sum(range(a, b+1)):
                ret.append(range(a, b+1))
                a += 1
            elif tsum > sum(range(a, b+1)):
                b += 1
            else:
                a += 1
        return ret

s = Solution()
print(s.FindContinuousSequence(45))