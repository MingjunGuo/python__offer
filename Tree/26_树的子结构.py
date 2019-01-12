# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        '''
        题目描述
        输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
        :param pRoot1:
        :param pRoot2:
        :return:
        '''
        # 递归思想
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self, Tree1, Tree2):
        if Tree2 == None:
            return True
        if Tree1 == None:
            return False
        if Tree1.val != Tree2.val:
            return False
        return self.DoesTree1HaveTree2(Tree1.left, Tree2.left) and self.DoesTree1HaveTree2(Tree1.right, Tree2.right)
