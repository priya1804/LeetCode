# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:46:57 2024

@author: priya
"""

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mx = (1 << maximumBit) - 1
        ans = []
        xors = 0

        for num in nums:
             xors ^= num
             ans.append(xors ^ mx)

        return ans[::-1]              
          