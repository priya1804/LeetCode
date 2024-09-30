# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:30:06 2024

@author: priya
"""

class CustomStack(object):
    
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        # Initialize the stack and add lists with the given max size.
        self.stack = [0] * maxSize
        self.add = [0] * maxSize
        self.current_size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.current_size < len(self.stack):
            self.stack[self.current_size] = x
            self.current_size += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.current_size == 0:
            return -1
        self.current_size -= 1
        result = self.stack[self.current_size] + self.add[self.current_size]
        if self.current_size > 0:
            self.add[self.current_size - 1] += self.add[self.current_size]
        self.add[self.current_size] = 0
        return result

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        limit = min(k, self.current_size) - 1
        if limit >= 0:
            self.add[limit] += val
