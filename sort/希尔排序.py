# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午5:32
# @Author : wu
"""
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法

与直接插入排序相比，只不过是将待排序列按某种规则分为几个子序列，分别对这几个子序列进行直接插入排序。这个规则的体现就是增量的选取，
如果增量为1，就是直接插入排序。

增量的选取规则：
gap = int(_len / 2)
while gap > 0:
    gap = int(gap/2)

增量序列的最后一个值一定取1
"""


def shell_sort(arr):
    _len = len(arr)
    gap = int(_len / 2)
    while gap > 0:
        # 这一大段逻辑是与直接插入排序一致的，只不过将 1 换成了 gap 而已
        for i in range(gap, _len):
            j = i - gap
            tmp = arr[i]
            while j >= 0 and tmp < arr[j]:
                arr[j + gap] = arr[j]
                j -= 1
            arr[j + gap] = tmp
        gap = int(gap / 2)
    return arr


data = [12, 34, 54, 2, 3]

print(shell_sort(data))
