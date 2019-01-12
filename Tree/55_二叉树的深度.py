# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        '''
        题目描述
        输入一棵二叉树，求该树的深度。
        从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
        :param pRoot:
        :return:
        '''
        if not pRoot:
            return 0
        if not pRoot.left and not pRoot.right:
            return 1
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
