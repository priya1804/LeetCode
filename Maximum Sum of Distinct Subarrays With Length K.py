# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:45:46 2024

@author: priya
"""

import collections

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        summ = 0
        distinct = 0
        count = collections.Counter()

        for i, num in enumerate(nums):
            summ += num
            count[num] += 1
            if count[num] == 1:
                distinct += 1
            if i >= k:
                count[nums[i - k]] -= 1
                if count[nums[i - k]] == 0:
                    distinct -= 1
                summ -= nums[i - k]
            if i >= k - 1 and distinct == k:
                ans = max(ans, summ)

        return ans
