# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        '''
        题目描述
        给定一个double类型的浮点数base和int类型的整数exponent。
        求base的exponent次方。
        :param base:
        :param exponent:
        :return:
        '''
        # step1: 永远首先检查输入合法性
        # step2: 注意代码的完整性
        if self.equal_zero(base) and exponent < 0:
            raise ZeroDivisionError
        ret = self.power_value(base, abs(exponent))
        if exponent < 0:
            ret = 1.0/ ret
        return ret


    def equal_zero(self, num):
        if abs(num-0.0) < 0.0000001:
            return True

    def power_value(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ret = self.power_value(base, exponent >> 1)
        ret *= ret
        if exponent & 1 == 1:
            ret *= base
        return ret

s = Solution()
# print(s.Power(0, -1))
print(s.Power(0, 1))
print(s.Power(34, 2))
print(s.Power(34, -2))


