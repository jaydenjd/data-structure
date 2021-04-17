# -*- coding: utf-8 -*-
# @Time   : 2021/4/5 下午7:26
# @Author : wu
"""
两种思路
1. 反转链表，然后依次写入队列
2. 将链表从头到尾依次写入栈中，然后再依次弹出写入另一个数组
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        反转链表，写入队列
        """
        if not listNode:
            return listNode
        cur = None
        while listNode:
            tmp = listNode.next
            listNode.next = cur
            cur = listNode
            listNode = tmp
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        """
        将链表从头到尾依次写入栈中，然后再依次弹出写入另一个数组
        Args:
            listNode:

        Returns:

        """
        if not listNode:
            return listNode
        stack = [], res = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            res.append(stack.pop())
        return res
