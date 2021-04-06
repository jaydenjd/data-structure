# -*- coding: utf-8 -*-
# @Time   : 2021/4/7 12:56 上午
# @Author : wu

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    """
    使用异或和与的知识
    1. a ^ a = 0
    2. a ^ 0 = a
    3. a & 1，结果要么为 1，要么为0
    用异或求解。异或运算的性质：
    任何一个数字异或它自己都等于0 。如果数组中只有一个数字出现过一次，其余数字都出现了两次；
    这样的话如果我们从头到尾依次异或数组中的每一个数字，那么最终的结果刚好是那个只出现一次的数字，因为那些出现两次的数字全部在异或中抵消掉了。
    如果能够把原数组分为两个子数组，在每个子数组中，包含一个只出现一次的数字，而其它数字都出现两次。在两个子数组中分别求出这两个只出现一次的数字。

    还是从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。因为其它数字都出现了两次，在异或中全部抵消掉了。
    由于这两个数字肯定不一样，那么这个异或结果肯定不为0，也就是说在这个结果数字的二进制表示中至少就有一位为1。
    我们在结果数字中找到第一个为1的位置，记为第N位。现在我们以第N 位是不是1 为标准把原数组中的数字分成两个子数组，
    第一个子数组中每个数字的第N 位都为1 ，而第二个子数组的每个数字的第N 位都为0 。
    现在我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其它数字都出现了两次。因此到此为止，所有的问题我们都已经解决
    """
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return None
        if len(array) == 2:
            return array
        res = 0
        index = 1
        for k in array:
            # res 是只出现一次的两个数的异或结果
            res ^= k
        # 当结果为1时，则是 res 中从右边起的第一个为1的位置
        while (res & index) == 0:
            # 左移操作，右边补0，例如 1<<1=10(2)，2<<1=100(4), 4<<1=1000(8)
            index <<= 1
        res1, res2 = 0, 0
        for k in array:
            # index 的结果是 1或 10 或 100 等 10... 这样的结果，设 1 在第 k 为。那么任意一个数 a，有 a&index 的结果，一定为 0 或者为 a
            # 当 a 的第 k 位为1时，那么结果是 a，否则结果为 0
            # 由以上，只出现一次的两个数，在第 k 位上，一定有一个是0，另一个是1。那么就可以把原数组分成两个子数组，每个子数组都包含一个只出现一次的数字
            if (k & index) == 0:
                res1 ^= k
            else:
                res2 ^= k
        return [res1, res2]


class SolutionHash:
    """ hash 的方式，理解起来比较简单，不作过多阐述"""
    def FindNumsAppearOnce(self, array):
        # write code here
        hash_map = dict()
        for i in array:
            hash_map[i] = hash_map.get(i, 0) + 1
        res = []
        for i in hash_map.keys():
            if hash_map[i] == 1:
                res.append(i)
            if len(res) == 2:
                break
        return res
