# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午8:41
# @Author : wu

"""
归并排序用的是分治法，把一个大问题化解为k个中问题，每个中问题再化解为k个小问题，直至问题化为最小可解的问题。对这些问题求解，再不断地合并结果，直至合并完毕。

归并排序可以看作一个分而治之的过程：先将整个序列分成两半，对每一半分别进行归并排序

时间复杂度：
平均：O(nlog2n),

空间复杂度：：O(n)
"""


def merge(left, right):
    res = []
    while left and right:
        res.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    res += left if left else right
    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2  # 即 int(len(arr)/2)
    # 归并排序前半段，再归并排序后半段
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    res = merge(left, right)
    return res


data = [12, 11, 13, 5, 6, 7]

print(merge_sort(data))
