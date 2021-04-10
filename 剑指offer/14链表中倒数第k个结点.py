# -*- coding: utf-8 -*-
# @Time   : 2021/4/5 下午8:07
# @Author : wu
"""
解题思路：

快慢双指针，先让一个指针指向头节点，先走K步，如果为空就返回空，反之，就再让一个指针从头节点出发，快慢指针一起走，直到快指针为空，输出慢指针

最后还需要注意的是，如果 k 大于指针长度，那么快指针走的步数应该是小于 k 的，这种情况下，应该返回空值

需要注意的特殊情况，均返回 None :

1. 链表为空
2. k 小于 1
3. k 大于链表长度

"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        # 链表为空 或者 k 小于 1
        if not pHead or k < 1:
            return None
        cursor = 1
        fast = slow = pHead
        while fast.next:
            if cursor >= k:
                slow = slow.next
            fast = fast.next
            cursor += 1
        # k 大于链表长度
        if cursor < k:
            return None
        return slow