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
        reverse = 0
        while tmp:
            tmp, mod = divmod(tmp, 10)
            if mod > 0:
                reverse += (reverse + mod) * 10
            else:
                reverse += tmp
        reverse = reverse if x > 0 else -reverse
        if reverse > 2 ** 31 - 1 or reverse < -2 ** 31:
            return 0
        return reverse
