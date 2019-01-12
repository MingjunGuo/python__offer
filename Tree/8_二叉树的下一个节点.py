# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        '''
        题目描述
        给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
        注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
        :param pNode:
        :return:
        '''
        # 共有三种情况：该节点是根节点：则下一个节点是右孩子本身（无左节点）或右孩子的左孩子
        #               该节点是左孩子，则下一个节点是对应的根节点
        #               该节点是右孩子， 则下一个节点是根节点到头（所属根节点是某根节点的左孩子）或者None
        if not pNode:
            return None
        # 情况1:
        if pNode.right != None:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        # 情况2：
        elif pNode.next is None:
            return None
        elif pNode.next.left == pNode:
            return pNode.next
        # 情况3
        else:
            while pNode.next:
                if pNode.next.left != pNode:
                    pNode = pNode.next
                else:
                    return pNode.next
            return None

