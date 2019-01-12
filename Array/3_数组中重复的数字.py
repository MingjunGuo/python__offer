# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        '''
        题目描述
        在一个长度为n的数组里的所有数字都在0到n-1的范围内。
        数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
        请找出数组中任意一个重复的数字。
        例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
        :param numbers: 输入的数组
        :param duplication: 将所有重复的数字放在这个列表中
        :return: true / false
        '''
        #  step1: 第一步永远是先判断输入是否合法，以及是否满足限制条件
        if numbers == None or len(numbers)<=0:
            return False
        for num in numbers:
            if num < 0 or num > len(numbers)-1:
                return False
        # step2: 空间复杂度为o(1)算法：更换位置后，数字应该出现在对应坐标位置，如果坐标位置和
        # 该位置大小一致，则说明重复
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False


test = [2,3,1,0,2,5,3]
s = Solution()
duplication = [0]
print(s.duplicate(test, duplication))



