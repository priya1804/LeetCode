# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:43:26 2024

@author: priya
"""

class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        seen = set()

        for num, i in sorted([(num, i) for i, num in enumerate(nums)]):
            if i in seen:
                continue
            seen.add(i - 1)
            seen.add(i + 1)
            seen.add(i)
            ans += num

        return ans
