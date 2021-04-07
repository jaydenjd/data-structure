# -*- coding: utf-8 -*-
# @Time   : 2021/4/7 下午1:01
# @Author : wu


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot):
        """
        递归解决，先遍历左子树，交换左右孩子，然后遍历右子树，交换左右孩子，类似于后序遍历

        代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
        """
        # write code here
        if pRoot:
            right = self.Mirror(pRoot.left)
            left = self.Mirror(pRoot.right)
            pRoot.right = right
            pRoot.left = left
            return pRoot
