# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        '''
        题目描述
        操作给定的二叉树，将其变换为源二叉树的镜像。
        :param root:
        :return:
        '''
        if root == None:
            return
        root.right, root.left = root.left, root.right
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

    def getMirror(self, root):
        if root == None:
            return
        newTree = TreeNode(root.val)
        newTree.left = self.getMirror(root.right)
        newTree.right = self.getMirror(root.left)
        return newTree