# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        '''
        题目描述
        请实现一个函数，将一个字符串中的每个空格替换成“%20”。
        例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
        :param s: 输入的字符串
        :return:
        '''
        # step1:判断输入合法性：
        if not s:
            return ''
        # step2:采用字符串内置replace 函数
        return s.replace(' ', '%20')

s = Solution()
print(s.replaceSpace('we are happy'))
print(s.replaceSpace('i love 1000'))