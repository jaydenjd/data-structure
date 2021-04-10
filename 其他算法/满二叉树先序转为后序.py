# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午2:42
# @Author : wu

"""

注意满二叉树的特点：

除了叶子结点，所有层结点数达到最大；如果高度为 n，则总结点数为 2 的 (n-1) 次方

题目秒速：
假设满二叉树 b 的先序遍历序列已经存在于数据组（在解题过程中，此数组名称可自定义，长度为 n），设计一个算法将其转换为后续遍历序列
"""


def pre2post(pre: list, pre_l: int, pre_r: int, post: list, post_l: int, post_r: int):
    """
    pre/post 是已初始化的列表，如 pre = [0]*n (n 表示结点总数）
    Args:
        pre: 先序数组
        pre_l: 先序数组的第一个结点下标
        pre_r: 先序数组的最后一个结点下标
        post: 后序数组
        post_l: 后序数组的第一个结点下标
        post_r: 后序数组的最后一个结点下标

    解题思路：
    本题已知先序遍历序列，则序列中第一个元素为根结点。将除去第一个元素之外的元素序列分成前后长度相等的两半，
    则一半为左子树上的结点，后一半为右子树上的结点。
    只需要将根结点移动到整个序列的末尾，然后分别递归去处理序列的前一半和后一半即可
    """
    if pre_l <= pre_r:
        print(post)
        post[post_r] = pre[pre_l]  # 将 pre[] 中的第一个元素放在 post[] 的末尾
        _len = int((pre_r - pre_l) / 2)
        # 递归处理前一半
        pre2post(pre, pre_l + 1, pre_l + _len, post, post_l, post_l + _len - 1)
        # 递归处理后一半
        pre2post(pre, pre_l + _len + 1, pre_r, post, post_l + _len, post_r - 1)


k = [0] * 7
pre2post([1, 2, 3, 4, 5, 6, 7], 0, 6, k, 0, 6)
print(k)
