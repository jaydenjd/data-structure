# -*- coding: utf-8 -*-
# @Time   : 2021/4/1 11:14 下午
# @Author : wu

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        利用二维数组由上到下，由左到右递增的规律；可选取右上角或者左下角的元素与 target 比较
        如选择左下角：
        当 target 小于元素 a[row][col] 时，那么 target 应该在元素 a 的上方
        当 target 大于元素 a[row][col] 时，那么 target 应该在元素 a 的右边
        """
        row = len(matrix) - 1
        col = 0
        while row >= 0 and col <= len(matrix[0]) - 1:
            if target == matrix[row][col]:
                return True
            # 在右边，故列+1
            if target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return False
