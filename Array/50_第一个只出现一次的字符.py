# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, string):
        '''
        题目描述
        在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
        并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
        :param s:
        :return:
        '''
        if not string:
            return -1
        count = {}
        loc = {}
        for k, s in enumerate(string):
            count[s] = count[s] + 1 if count.get(s) else 1
            loc[s] = loc[s] if loc.get(s) else k
        ret = float('inf')
        for k in loc.keys():
            if count[k] == 1 and loc[k] < ret:
                ret = loc[k]
        return ret

string = 'google'
s = Solution()
print(s.FirstNotRepeatingChar(string))