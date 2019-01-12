# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        '''
        题目描述
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
        打印能拼接出的所有数字中最小的一个。
        例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
        :param numbers: 正整数数组
        :return: 最小的数
        '''
        # Step1：永远先判断输入是否合法
        if not numbers:
            return ''
        strNum = [str(num) for num in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if strNum[i]+strNum[j] > strNum[j]+strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]
        return ''.join(strNum)

numbers = [3,12,45,67,1098]
numbers1 = []
numbers2 = [1,1]
s = Solution()
print(s.PrintMinNumber(numbers))
print(s.PrintMinNumber(numbers1))
print(s.PrintMinNumber(numbers2))
