# -*- coding:utf-8 -*-
class Solution:
    def EntryNodeOfLoop(self, pHead):
        '''
        题目描述
        给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
        :param pHead:
        :return:
        '''
        # step1: 永远首先判断输入合法性
        if pHead == None or pHead.next == None:
            return None
        # 快慢两个指针，快指针一次走两步，慢指针一次走一步
        onestep = pHead
        twostep = pHead
        while twostep:
            onestep = onestep.next
            twostep = twostep.next.next
            if onestep == twostep:
                onestep = pHead
                while onestep != twostep:
                    onestep = onestep.next
                    twostep = twostep.next
                return onestep
        return None