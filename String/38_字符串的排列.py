# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        '''
        题目描述
        输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
        输入描述:
        输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
        :param ss:字符串
        :return:
        '''
        # step1: 首先检查输入合法性：
        if not ss or len(ss)>9:
            return ''
        # step2: 问题的分解，采用递归：
        ret = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):
                if j not in ret:
                    ret.append(j)
        return ret

s = Solution()
print(s.Permutation('abc'))