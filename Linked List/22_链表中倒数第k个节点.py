# -*- coding:utf-8 -*-
class ListNode:
    def _init_(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # step1: 首先检查输入合法性：其实和代码鲁棒性有关，即考虑空链表和k为0的情况
        if not head or k < 1:
            return None
        move = head
        for i in range(k - 1):
            if move.next:
                move = move.next
            else:
                return None
        while move.next:
            move = move.next
            head = head.next
        return head