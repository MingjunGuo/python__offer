# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        '''
        题目描述
        输入两个链表，找出它们的第一个公共结点。
        :param pHead1:
        :param pHead2:
        :return:
        '''
        # step1: 代码鲁棒性：永远首先检查输入合法性
        if not pHead1 or not pHead2:
            return None
        # step2: 长链表先走长的步骤，然后两个链表一次走
        length1 = length2 = 0
        move1, move2 = pHead1, pHead2
        while move1:
            length1 += 1
            move1 = move1.next
        while move2:
            length2 += 1
            move2 = move2.next
        while length1 > length2:
            length1 -= 1
            pHead1 = pHead1.next
        while length2 > length1:
            length2 -= 1
            pHead2 = pHead2.next
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            pHead1, pHead2 = pHead1.next, pHead2.next
        return None