# -*- coding: utf-8 -*-
# @Time   : 2021/4/5 下午7:34
# @Author : wu
class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, node):
        # write code here
        self.stack_in.append(node)

    def pop(self):
        # return xx
        if self.stack_out:
            return self.stack_out.pop()
        if not self.stack_in:
            return -1
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
