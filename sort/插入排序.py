# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu

"""
算法思想:
每趟将一个待排序的关键字按照其值的大小，插入到已经排序好的部分有序序列的适当位置上，直到所有待排关键字都被插入到有序序列中为止

时间复杂度：O(n^2）

空间复杂度：：O(1)
"""

def insert_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        tmp = data[i]
        while j >= 0 and tmp < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = tmp

    return data


data = [1, 4, 5, 2, 3]
print(insert_sort(data))


