# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        '''
        题目描述
        从上往下打印出二叉树的每个节点，同层节点从左至右打印。
        :param root:
        :return:
        '''
        # 其实就是层次遍历（广度优先)， 递归有点意思
        if root == None:
            return []
        myQueue = []
        node = root
        myQueue.append(node)
        result = []
        while myQueue:
            node = myQueue.pop(0)
            result.append(node.val)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

        return result



