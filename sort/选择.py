# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu


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
