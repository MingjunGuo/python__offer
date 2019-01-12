# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, ss):
        '''
        题目描述
        将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
        数值为0或者字符串不是一个合法的数值则返回0。
        输入描述:
        输入一个字符串,包括数字字母符号,可以为空
        输出描述:
        如果是合法的数值表达则返回该数字，否则返回0
        :param ss:
        :return:
        '''
        # step1: 永远首先判断输入合法性
        if not ss:
            return 0
        # step2: 分为纯数字/数字+字母/字母两种情况，注意符号位。
        ret = 0
        flag = 0
        num_occur = False
        for k, s in enumerate(ss):
            if s.isdigit():
                val = ord(s)-ord('0')
                ret = ret * 10 + val
                num_occur = True
            else:
                if s == '+' and k == 0:
                    flag = 1
                elif s == '-' and k == 0:
                    flag = -1
                elif num_occur:
                    return 0
        return ret if flag >= 0 else -ret
