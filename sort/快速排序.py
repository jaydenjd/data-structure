# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午7:29
# @Author : wu
"""
快速排序是一种非常高效的排序算法，采用 “分而治之” 的思想，把大的拆分为小的，小的拆分为更小的。其原理是，对于给定的记录，选择一个基准数，通过一趟排序后，将原序列分为两部分，使得前面的比后面的小，然后再依次对前后进行拆分进行快速排序，递归该过程，直到序列中所有记录均有序。

步骤
设当前待排序序列为R[low:high]，其中low ≤ high，如果待排序的序列规模足够小，则直接进行排序，否则分3步处理。

1、分解
在R[low:high]中选定一个元素R[pivot]，以此为标准将要排序的序列划分为两个序列R[low:pivot-1]与R[pivot+1：high]，并使序列R[low:pivot-1]中所有元素的值小于等于R[pivot]，序列R[pivot+1：high]所有的值大于R[pivot]，此时基准元素以位于正确位置，它无需参加后续排序。

2、递归
对于子序列R[low:pivot-1]与R[pivot+1：high]，分别调用快速排序算法来进行排序。

3、合并
由于对序列R[low:pivot-1]与R[pivot+1：high]的排序是原地进行的，所以R[low:pivot-1]与R[pivot+1：high]都已经排好序后，不需要进行任何计算，就已经排好序。

注：基准元素，一般来说选取有几种方法

取第一个元素
取最后一个元素
取第中间位置元素
取第一个、最后一个、中间位置3者的中位数元素

时间复杂度：
最好：O(nlog2n), 最差：O(n^2)， 平均：O(nlog2n),

空间复杂度：：O(log2n)
"""


def quick_sort(arr, low, high):
    """
    Args:
        arr: 排序数组
        low: 起始索引
        high: 结束索引

    Returns:
    """
    if low >= high:
        return arr
    i, j = low, high
    pivot = arr[low]
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot
    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)


data = [1, 4, 5, 2, 3]
quick_sort(data, 0, len(data) - 1)
print(data)
