
"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。

链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            return self.del_node(root)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def del_node(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        p = node
        s = node.left
        while s.right:
            p = s
            s = s.right
        node.val = s.val
        if p != node:
            p.right = s.left
        else:
            # 可能 s 在一开始就没有右子树
            p.left = s.left
        return node
