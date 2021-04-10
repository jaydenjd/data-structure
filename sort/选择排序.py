# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu
"""
算法思想：
选择类排序的主要动作是"选择"，简单选择排序采用最简单的选择方式，从头到尾顺序扫描序列，找出最小（或最大）的一个关键字，和第一个关键字交换
接着从剩下的关键字中继续这种选择和交换，最终使序列有序
"""


def select_sort(arr):
    n = len(arr)
    for i in range(n):
        _min = i
        for j in range(i, n):
            if arr[j] < arr[_min]:
                _min = j
        if _min != i:
            arr[i], arr[_min] = arr[_min], arr[i]
    return arr


data = [1, 4, 5, 2, 3]
print(select_sort(data))
