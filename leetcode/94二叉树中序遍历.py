# -*- coding: utf-8 -*-
# @Time   : 2021/3/29 11:48 下午
# @Author : wu
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        stack = []
        res = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                if node.val:
                    res.append(node.val)
                node = node.right

        return res


class SolutionRecursion:
    """使用递归方式"""

    def inorderTraversal(self, root: TreeNode):
        res_list = []
        if not root:
            return []
        self.pre_traversal(root, res_list)
        return res_list

    def pre_traversal(self, node: TreeNode, res_list: []):
        if node:
            self.pre_traversal(node.left, res_list)
            res_list.append(node.val)
            self.pre_traversal(node.right, res_list)
