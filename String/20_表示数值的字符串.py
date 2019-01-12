# -*- coding:utf-8 -*-
class Solution:
    def isNumeric(self, s):
        '''
        题目描述
        请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
        但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        :param s: 输入字符串
        :return:
        '''
        # step1: 首先判断输入合法性
        if not s:
            return False
        # step2:以E/e为界，进行分开判断
        aList = [i.lower() for i in s]
        if 'e' in aList:
            index = aList.index('e')
            before = aList[:index]
            behind = aList[index+1:]
            if len(behind)==0 or '.' in behind:
                return False
            isbefore = self.is_digit(before)
            isbehind = self.is_digit(behind)
            return isbefore and isbehind
        else:
            isaList = self.is_digit(aList)
            return isaList

    def is_digit(self, string):
        is_allow = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', 'e']
        dotNum = 0
        for i in range(len(string)):
            if string[i] not in is_allow:
                return False
            if string[i] == '.':
                dotNum += 1
            if string[i] in '+-' and i != 0:
                return False
        if dotNum > 1:
            return False
        return True

s = Solution()
print(s.isNumeric('1a3.14'))
print(s.isNumeric('1.2.3'))
print(s.isNumeric('+-5'))
print(s.isNumeric('+56.3e-789'))
