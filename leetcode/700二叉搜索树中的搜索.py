# -*- coding: utf-8 -*-
# @Time   : 2021/4/13 8:24 上午
# @Author : wu
"""
二叉搜索树（又叫二叉查找树或二叉排序树）的定义：

二叉排序树或者是空树，或者是满足以下兴致的二叉树：
1）若它的左子树不空，则左子树上所有关键字的值均不大于（不小于）根关键字的值
2）若它的右子树不空，则右子树上所有关键字的值均不小于（不大于）根关键字的值
3）左右子树又各是一颗二叉搜索树

说明：由二叉搜索树的定义可以知道，如果输出二叉排序树的中序遍历序列，则这个序列是非递减（非递增）有序的。
     如题目不做说明，排序二叉树结点关键字按"左小右大"分布（数据结构高分笔记2021-天勤第10版-P284)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if not root:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
