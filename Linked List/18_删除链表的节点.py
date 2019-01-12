# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x=None):
        ListNode.val = x
        ListNode.next = None


class Solution:
    def deleteDuplication(self, pHead):
        '''
        题目描述
        在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
        例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
        :param pHead:
        :return:
        '''
        first = ListNode(-1)
        first.next = pHead
        last = first
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and val == pHead.val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next
        return first.next

s = Solution()
singleNode = ListNode()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(s.deleteDuplication(singleNode))
print(s.deleteDuplication(node1))
