# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        '''
        题目描述
        请实现两个函数，分别用来序列化和反序列化二叉树
        :param root:
        :return:
        '''
        result = []

        def preOrder(root):
            if root:
                result.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
            else:
                result.append('#')

        preOrder(root)
        return ','.join(result)

    def Deserialize(self, s):
        '''
        题目描述
        请实现两个函数，分别用来序列化和反序列化二叉树
        :param s:
        :return:
        '''
        s = s.split(',')
        num = [-1]

        def Change(num):
            num[0] += 1
            if num[0] < len(s):
                if s[num[0]] == '#':
                    return None
                root = TreeNode(int(s[num[0]]))
                root.left = Change(num)
                root.right = Change(num)
                return root
            else:
                return None

        return Change(num)
