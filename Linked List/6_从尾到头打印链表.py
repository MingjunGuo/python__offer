# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        '''
        题目描述
        输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
        :param listNode:
        :return:
        '''
        stack = []
        while listNode:
            stack.insert(0, listNode.val)
            listNode = listNode.next
        return stack


s = Solution()
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node1.next = node2
node2.next = node3

singlenode = ListNode(8)
test = ListNode()

print(s.printListFromTailToHead(node1))
print(s.printListFromTailToHead(singlenode))
print(s.printListFromTailToHead(test))
