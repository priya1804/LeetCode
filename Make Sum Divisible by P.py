# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:53:27 2024

@author: priya
"""

class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        n = len(nums)
        min_length = n
        prefix_sum = 0
        prefix_sums = {0: -1}  # Equivalent to unordered_map in C++

        for i in range(n):
            prefix_sum = (prefix_sum + nums[i]) % p
            target = (prefix_sum - remainder + p) % p

            if target in prefix_sums:
                min_length = min(min_length, i - prefix_sums[target])

            prefix_sums[prefix_sum] = i

        return -1 if min_length == n else min_length