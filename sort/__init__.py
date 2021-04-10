# -*- coding: utf-8 -*-
# @Time   : 2021/3/13 5:32 下午
# @Author : wu

def reverse(x: int) -> int:
    if x == 0:
        return 0
    res = 0
    x = abs(x)
    n = len(str(x))
    k = n - 1
    for i in range(0, n):
        print(int((x / 10 ** i)) % 10)
        res += (int((x / 10 ** i)) % 10) * (10 ** k)
        k -= 1
    return res if x > 0 else -res


print(reverse(-341))
