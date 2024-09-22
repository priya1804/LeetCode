# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:37:23 2024

@author: priya
"""

class Solution(object):
    def findKthNumber(self, n, k): 
        ans = 1
        i = 1
        while i < k:
            gap = self._getGap(ans, ans + 1, n)
            if i + gap <= k:
                i += gap
                ans += 1
            else:
                i += 1
                ans *= 10
        return ans

    def _getGap(self, a, b, n):
        gap = 0
        while a <= n:
            gap += min(n + 1, b) - a
            a *= 10
            b *= 10
        return gap
      
        