# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:56:21 2024

@author: priya
"""

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}
        for i in sorted(arr):
            if i not in rank:
                rank[i] = len(rank) + 1
        return [rank[i] for i in arr]

    """
    :type arr: List[int]
    :rtype: List[int]
    """
