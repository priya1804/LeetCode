# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:57:57 2024

@author: priya
"""

class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        l = 1
        r = max(quantities)

        def numStores(m):
            return sum((q - 1) // m + 1 for q in quantities)

        while l < r:
            m = (l + r) // 2
            if numStores(m) <= n:
                r = m
            else:
                l = m + 1

        return l
