# -*- coding: utf-8 -*-
# @Time   : 2021/4/7 12:26 上午
# @Author : wu

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        标签：链表
        1. 将两个链表看成是相同长度的进行遍历，如果一个链表较短则在前面补 00，比如 987 + 23 = 987 + 023 =
        1010
        2. 每一位计算的同时需要考虑上一位的进位问题，而当前位计算结束后同样需要更新进位值
        3. 如果两个链表全部遍历完毕后，进位值为 11，则在新链表最前方添加节点 11
        4. 小技巧：对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 pre，该指针的下一个节点指向真正
        的头
        5. 结点head。使用预先指针的目的在于链表初始化时无可用节点值，而且链表构造过程需要指针移动，进而会导致头指
        针丢失，无法返回结果。
        """
        res = ListNode()  # 相当于创建了一个带头结点的链表
        tmp = res  # 创建一个临时指针去移动，而保持 res 始终指向头结点
        mod = 0
        while l1 or l2 or mod:
            cnt = 0
            if l1:
                cnt += l1.val
                l1 = l1.next
            if l2:
                cnt += l2.val
                l2 = l2.next
            cnt += mod
            mod, num = divmod(cnt, 10)  # 逢10则往右边进1
            tmp.next = ListNode(num)
            tmp = tmp.next
        return res.next
