# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, string):
        '''
        题目描述
        将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
        要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
        输入描述:
        输入一个字符串,包括数字字母符号,可以为空
        输出描述:
        如果是合法的数值表达则返回该数字，否则返回0
        :param s:
        :return:
        '''
        if not string:  # 空字符返回异常
            return 0
        flag = 0  # 用来表示第一个字符是否为+、-
        ret = 0  # 结果
        digit_occur = False
        for k, s in enumerate(string):
            if s.isdigit():  # 数字直接运算
                val = ord(s) - ord('0')
                ret = ret * 10 + val
                digit_occur = True
            else:
                if not flag:
                    if s == '+' and k == 0:  # 避免中间出现+、-
                        flag = 1
                    elif s == '-' and k == 0:
                        flag = -1
                    elif digit_occur:
                        return 0
        return ret if flag >= 0 else -ret


s = Solution()
print('abc', s.StrToInt('abc'))
print('-abc', s.StrToInt('-abc'))
print('a-bc', s.StrToInt('a-bc'))
print('ab10c', s.StrToInt('ab10c'))
print('ab0c', s.StrToInt('ab0c'))
print('1a33', s.StrToInt('1a33'))