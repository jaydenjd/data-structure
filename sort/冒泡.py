# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu

def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def bubble_sort(data):
    i = len(data) - 1
    while i > 0:
        j = 0
        while j < i - 1:
            if data[j] > data[j + 1]:
                swap(data, j, j + 1)
            j += 1
        i -= 1

    return data


data = [1, 4, 5, 2, 3]
print(bubble_sort(data))
