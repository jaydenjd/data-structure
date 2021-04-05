# -*- coding: utf-8 -*-
# @Time   : 2021/4/4 下午4:34
# @Author : wu


def fib_non_cur(n):
    """非递归"""
    n1 = 0
    n2 = 1
    k = 0
    if n <= 1:
        return n
    for i in range(2, n + 1):
        k = n1 + n2
        n1 = n2
        n2 = k
    return k


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(10):
    print(fib(i))
