# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:01:16 2024

@author: priya
"""

class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        ans = 1
        for i, n in enumerate(nums):
            while n - k > nums[left] + k:
                left += 1
            ans = ans if ans > i - left + 1 else  i - left + 1
        return ans