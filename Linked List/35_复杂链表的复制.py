# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        '''
        题目描述
        输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
        返回结果为复制后复杂链表的head。
        （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
        :param pHead:
        :return:
        '''
        copy_pHead = self.Clone_Nodes(pHead)
        copy_Link = self.Set_Nodes(copy_pHead)
        split_nodes = self.Split_Nodes(copy_Link)
        return split_nodes

    def Clone_Nodes(self, pHead):
        # step1: 用于结点复制
        head = pHead
        while head:
            tmp = RandomListNode(head.label)
            tmp.next = head.next
            head.next = tmp
            head = tmp.next
        return pHead

    def Set_Nodes(self, pHead):
        # step2: 用于特殊指针复制
        head = pHead
        while head:
            tmp = head.next
            if head.random:
                tmp.random = head.random.next
            head = tmp.next
        return pHead

    def Split_Nodes(self, pHead):
        # step3: 用于结点拆分
        # 结点拆分
        pNode = pHead
        pCloneHead = pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next, pCloneNode = pNode.next, pCloneNode.next
            pNode.next, pNode = pCloneNode.next, pNode.next
        return pCloneHead


