# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:29:14 2024

@author: priya
"""

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        patterns = [tuple(a ^ row[0] for a in row) for row in matrix]
        return max(Counter(patterns).values())