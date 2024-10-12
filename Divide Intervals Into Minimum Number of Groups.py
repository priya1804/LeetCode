# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:12:52 2024

@author: priya
"""

class Solution(object):
    def minGroups(self, intervals):
        q = []
        for left, right in sorted(intervals):
            if q and q[0] < left:
                heappop(q)
            heappush(q, right)
        return len(q)
        
        