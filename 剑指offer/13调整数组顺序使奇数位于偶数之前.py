# -*- coding: utf-8 -*-
# @Time   : 2021/4/8 12:42 上午
# @Author : wu
"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
示例1
输入
复制
[1,2,3,4]
返回值
复制
[1,3,2,4]
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def reOrderArray(self, array):
        # write code here
        """类似插入排序"""
        for i in range(1, len(array)):
            # 如果是偶数，不需要动
            if array[i] % 2 == 0:
                continue
            j = i - 1
            while j >= 0:
                if array[j] % 2 == 0:
                    self.swap(array, j, j + 1)
                # 碰到偶数，直接中断即可
                else:
                    break
                j -= 1
        return array
