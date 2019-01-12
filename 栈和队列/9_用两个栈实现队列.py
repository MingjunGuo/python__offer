# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        '''
        题目描述
        用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
        :param node:
        :return:
        '''
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'
