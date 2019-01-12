# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack and self.minstack[-1] < node:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(node)

    def pop(self):
        # write code here
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()
        return None

    def top(self):
        # write code here
        return self.stack[-1] if self.stack else None

    def min(self):
        # write code here
        '''
        题目描述
        定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
        :return:
        '''
        return self.minstack[-1] if self.minstack else None