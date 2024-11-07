# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:11:19 2024

@author: priya
"""

class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        return max(sum(c >> i & 1 for c in candidates) for i in range(24))