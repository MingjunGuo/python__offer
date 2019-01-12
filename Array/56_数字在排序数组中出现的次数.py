# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, nums, k):
        '''
        题目描述
        统计一个数字在排序数组中出现的次数。
        :param data: 排序数组
        :param k: 需要统计的数字
        :return:
        '''
        # Step1: 永远先判断输入是否合法
        if not nums:
            return 0
        # Step2: 使用二分法进行查找, 分别找到数组中第一个和最后一个出现该值的坐标，然后相减
        first = self.get_first_k(nums, k)
        last = self.get_last_k(nums, k)
        if first < 0 and last < 0:
            return 0
        if first < 0 or last < 0:
            return 1
        return last-first+1

    def get_first_k(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if k == nums[mid]:
                if mid > left and nums[mid-1]==k:
                    right = mid-1
                else:
                    return mid
            elif k > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get_last_k(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if k == nums[mid]:
                if mid<right and nums[mid+1]==k:
                    left = mid+1
                else:
                    return mid
            elif k > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

a = [1,2,3,3,3,3,4,5]
a1 = []
a2 = [1]
s = Solution()
print(s.GetNumberOfK(a, 3))
print(s.GetNumberOfK(a1, 0))
print(s.GetNumberOfK(a2, 0))
