# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k == 0:
            return None
        self.treeNode = []

        def inorder(pRoot):
            if pRoot.left:
                inorder(pRoot.left)
            self.treeNode.append(pRoot)
            if pRoot.right:
                inorder(pRoot.right)

        inorder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]

