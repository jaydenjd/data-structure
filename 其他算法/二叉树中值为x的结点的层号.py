# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午3:10
# @Author : wu
"""
题目描述：
假设二叉树采用二叉链表存储结构，设计一个算法，求二叉树 b 中值为 x 的结点的层号
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


k = 1


def leno(head: TreeNode, x):
    global k
    if not head:
        return -1
    if head.val == x:
        return k
    k += 1
    leno(head.left, x)
    leno(head.right, x)
    k -= 1
