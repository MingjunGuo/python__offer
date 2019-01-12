# -*- coding:utf-8 -*-
class BinNode():
    def __init__(self, val):
        self.lchild = None
        self.rchild = None
        self.val = val

    def preOrder(self, root):
        # 先序遍历：递归
        if root == None:
            return
        print(root.val)
        self.preOrder(root.lchild)
        self.preOrder(root.rchild)

    def inOrder(self, root):
        # 中序遍历：递归
        if root == None:
            return
        self.inOrder(root.lchild)
        print(root.val)
        self.inOrder(root.rchild)

    def postOrder(self, root):
        # 后续遍历：递归
        if root == None:
            return
        self.postOrder(root.lchild)
        self.postOrder(root.rchild)
        print(root.val)

    def preOrder_1(self, root):
        # 先序遍历：非递归
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                # 从根节点开始， 一直找它的左子树
                print(node.val)
                myStack.append(node)
                node = node.lchild
            # while 结束表示当前节点node 为空，即前一个节点没有左子树了
            node = myStack.pop()
            node = node.rchild

    def inOrder_1(self, root):
        # 中序遍历：非递归
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            # while结束，表示当前节点node为空，即前一个节点没有左子树了
            node = myStack.pop()
            print(node.val)
            node = node.rchild

    def postOrder_1(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            # 这个while循环功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().val)

    def levelOrder(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)



