# -*- coding: utf-8 -*-
# @Time   : 2021/3/29 11:08 下午
# @Author : wu

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """使用栈的方式，非递归"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res_list, stack = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val:
                res_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res_list


class SolutionRecursion:
    """使用递归方式"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res_list, stack = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val:
                res_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res_list
