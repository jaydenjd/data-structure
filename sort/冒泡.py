# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


data = [1, 4, 5, 2, 3]
print(bubble_sort(data))
