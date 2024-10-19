# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 08:33:16 2024

@author: priya
"""

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '0'
        
        midIndex = pow(2, n - 1)  # 1-indexed
        
        if k == midIndex:
            return '1'
        
        if k < midIndex:
            return self.findKthBit(n - 1, k)
        
        return '1' if self.findKthBit(n - 1, midIndex * 2 - k) == '0' else '0'
