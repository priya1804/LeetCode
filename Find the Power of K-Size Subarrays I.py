# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:17:12 2024

@author: priya
"""

class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        arr = [0] * (n - k + 1)
        count = 0

        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                count += 1

        arr[0] = nums[k - 1] if count == k - 1 else -1

        for i in range(1, n - k + 1):
            if nums[i] == nums[i - 1] + 1:
                count -= 1
            if nums[i + k - 1] == nums[i + k - 2] + 1:
                count += 1
            arr[i] = nums[i + k - 1] if count == k - 1 else -1

        return arr
