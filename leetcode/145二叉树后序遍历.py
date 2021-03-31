# -*- coding: utf-8 -*-
# @Time   : 2021/3/29 11:27 下午
# @Author : wu

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        """
        后序打印二叉树（非递归）
        原理：
            逆后续遍历序列是先序遍历过程中对左右字数遍历顺序交换所得到的结果
            将逆后续遍历的结果存到一个栈里，然后依次出栈，得到的就是后续遍历的结果
        思路：
            使用两个栈结构
            第一个栈进栈顺序：左节点 -> 右节点 -> 根节点
            第一个栈弹出顺序： 根节点 -> 右节点 -> 左节点(先序遍历栈弹出顺序：根 -> 左 -> 右)
            第二个栈存储为第一个栈的每个弹出依次进栈
            最后第二个栈依次出栈
        :param root:
        :return:
        """
        res_list, stack1, stack2 = [], [], []
        if not root:
            return []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            if not node:
                continue
            if node.val:
                res_list.append(node.val)

        return res_list


class SolutionRecursion:
    """使用递归方式"""

    def postorderTraversal(self, root: TreeNode):
        res_list = []
        if not root:
            return []
        self.pre_traversal(root, res_list)
        return res_list

    def pre_traversal(self, node: TreeNode, res_list: []):
        if node:
            self.pre_traversal(node.left, res_list)
            self.pre_traversal(node.right, res_list)
            res_list.append(node.val)
