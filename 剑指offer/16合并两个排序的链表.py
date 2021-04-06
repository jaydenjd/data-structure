# -*- coding: utf-8 -*-
# @Time   : 2021/4/7 1:17 上午
# @Author : wu
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead = ListNode(0)  # 创建一个头结点
        tmp = pHead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        if pHead1:
            tmp.next = pHead1
        if pHead2:
            tmp.next = pHead2
        return pHead.next
