# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        '''
        题目描述
        输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
        例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
        :param numbers:
        :return:
        '''
        # step1: 永远首先判断输入合法性
        if not numbers:
            return ''
        # step2: 使用冒泡排序
        strNum = [str(i) for i in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]
        return ''.join(strNum)