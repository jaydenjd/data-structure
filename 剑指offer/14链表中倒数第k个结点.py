# -*- coding: utf-8 -*-
# @Time   : 2021/4/5 下午8:07
# @Author : wu
"""
解题思路：

快慢双指针，先让一个指针指向头节点，先走K步，如果为空就返回空，反之，就再让一个指针从头节点出发，快慢指针一起走，直到快指针为空，输出慢指针

最后还需要注意的是，如果 k 大于指针长度，那么快指针走的步数应该是小于 k 的，这种情况下，应该返回空值t 

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
    def FindKthToTail(self, pHead, k):
        # write code here
        if not pHead or k <= 0:
            return None
        cnt = 1
        slow = fast = pHead
        while fast.next:
            if cnt >= k:
                slow = slow.next
            cnt += 1
            fast = fast.next
        if cnt < k:
            return None
        return slow
