# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:32:18 2024

@author: priya
"""

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = -1
        for v in nums:
            t = 0
            while v in s:
                v *= v # Square the current number
                t += 1 # Increment the streak length
            if t > 1: # If the streak contains at least 2 elements
                ans = max(ans, t) # Update the maximum streak length
        return ans