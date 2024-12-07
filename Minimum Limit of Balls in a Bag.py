# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:42:11 2024

@author: priya
"""

import bisect

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDivide(mid):
            # Check if we can make all elements <= mid with maxOperations
            operations = 0
            for num in nums:
                # Calculate the number of splits needed
                operations += (num - 1) // mid
                if operations > maxOperations:
                    return False
            return True

        # Binary search on the penalty
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid  # Try for a smaller maximum size
            else:
                left = mid + 1  # Increase the size
        return left
