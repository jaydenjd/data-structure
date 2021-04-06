# -*- coding: utf-8 -*-
# @Time   : 2021/4/6 11:34 下午
# @Author : wu
class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """
        异或运算有这样的特性：
        交换律：a ^ b == b ^ a
        相同数字异或为零：a ^ a == 0
        数字异或零为该数字：a ^ 0 == a
        """

        target = 0
        for n in nums:
            target ^= n
        return target
