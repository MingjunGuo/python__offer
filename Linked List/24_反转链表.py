# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        if pHead.next == None:
            return pHead
        then = pHead.next
        last = then.next
        first = pHead
        first.next = None
        while then:
            then.next = first
            first = then
            then = last
            if last:
                last = last.next
        return first