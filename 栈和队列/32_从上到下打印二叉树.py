# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        '''
        题目描述
        从上往下打印出二叉树的每个节点，同层节点从左至右打印。
        :param root:
        :return:
        '''
        ret = []
        if not root:
            return ret
        myQueue = []
        myQueue.append(root)
        while myQueue:
            node = myQueue.pop(0)
            ret.append(node.val)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
        return ret