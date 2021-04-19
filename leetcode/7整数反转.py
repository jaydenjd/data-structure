# -*- coding: utf-8 -*-
# @Time   : 2021/4/10 下午10:19
# @Author : wu
"""
整数反转
如输入 234，shuchu  432
"""


class Solution:
    def reverse(self, x: int) -> int:
        tmp = abs(x)
        num = 0
        while tmp:
            tmp, n = divmod(tmp, 10)
            if tmp != 0:
                num = (num + n) * 10
            else:
                num += n
        if num > 2 ** 31 - 1 or num < -2 ** 31:
            return 0
        return num if x > 0 else -num
