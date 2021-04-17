# -*- coding: utf-8 -*-
# @Time   : 2021/4/17 下午5:40
# @Author : wu
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    import sys
    tmp = -sys.maxsize  # 没有给出边界，只能取系统的最小值了，始终记录着当前所访问节点的前驱的值

    def isValidBST(self, root: TreeNode) -> bool:
        """
        对于二叉排序树来说，中序遍历序列为递增有序序列。因此，对给定的二叉树进行中序遍历，
        如果能保证前一个值不比后一个值大，则证明该二叉树是一颗二叉排序树
        """
        if not root:
            return True  # 空树也是一颗二叉搜索树
        is_left_bst = self.isValidBST(root.left)  # 遍历左子树
        # 判断左子树是否为二叉搜索树，或者判断 tmp 是否依次递增
        if not is_left_bst or self.tmp >= root.val:
            return False
        self.tmp = root.val  # 将当前所访问节点的值赋值给 tmp
        return self.isValidBST(root.right)  # 遍历右子树
