# -*- coding:utf-8 -*-
class ListNode:
    def _init_(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        '''
        题目描述
        输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
        :param pHead1:
        :param pHead2:
        :return:
        '''
        # step1: 永远首先检查代码的鲁棒性
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        # step2: 使用递归解决问题，就只需要用条件判断语句，不需要用while / for 等循环语句
        if pHead1.val <= pHead2.val:
            ret = pHead1
            ret.next = self.Merge(pHead1.next, pHead2)
        else:
            ret = pHead2
            ret.next = self.Merge(pHead1, pHead2.next)
        return ret