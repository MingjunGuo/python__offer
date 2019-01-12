# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        '''
        题目描述
        输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
        假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
        :param pre:
        :param tin:
        :return:
        '''
        # step1: 检查代码的鲁棒性：永远先检查输入合法性
        if not pre or not tin:
            return None
        index = tin.index(pre[0])
        root = TreeNode(pre[0])
        left = tin[:index]
        right = tin[index+1:]
        root.left = self.reConstructBinaryTree(pre[1:len(left)+1], left)
        root.right = self.reConstructBinaryTree(pre[len(left)+1:], right)
        return root
