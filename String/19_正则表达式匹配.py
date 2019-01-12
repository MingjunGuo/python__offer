# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        '''
        题目描述
        请实现一个函数用来匹配包括'.'和'*'的正则表达式。
        模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
        在本题中，匹配是指字符串的所有字符匹配整个模式。
        例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
        :param s: 输入字符串
        :param pattern: 与之进行比较的字符串
        :return:
        '''
        # step1:永远先判断输入合法性
        # step2：分为四种情况：直接相等，patter[1]==*,pattern[0]==./pattern[0]==s[0],其他
        if pattern==s:
            return True
        if len(pattern)>1 and pattern[1]=='*':
            if s and (s[0]==pattern[0] or pattern[0]=='.'):
                return self.match(s[1:], pattern) or self.match(s, pattern[2:])
            else:
                return self.match(s, pattern[2:])
        elif s and pattern and (s[0]==pattern[0] or pattern[0]=='.'):
            return self.match(s[1:], pattern[1:])
        return False

s = Solution()
print(s.match('aaa', 'a.a'))
print(s.match('aaa', 'ab*ac*a'))
print(s.match('aaa', 'aa.a'))
print(s.match('aaa', 'ab*a'))
print(s.match('',','))
print(s.match(' ', '*'))
print(s.match(' ', ','))