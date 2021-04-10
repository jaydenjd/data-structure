# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午9:32
# @Author : wu


def radix_sort(s, max_num=None):
    """基数排序"""
    i = 0
    if max_num:
        cycle = len(str(max_num))
    else:
        cycle = len(str(max(s)))
    while i < cycle:
        buckets = [[] for _ in range(10)]
        for k in s:

            buckets[int(k / (10 ** i)) % 10].append(k)
        s.clear()
        for n in buckets:
            for m in n:
                s.append(m)
        i += 1
    return s


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(a, 345345)
    print(a)
