# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu


def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def select_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            swap(data, min_index, i)

    return data


data = [1, 4, 5, 2, 3]
print(select_sort(data))
