# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:59:11 2024

@author: priya
"""

class Solution:
    def maxWidthRamp(self, nums):
        # Create a list of indexes sorted by their values in nums
        sorted_indexes = sorted(range(len(nums)), key=lambda i: nums[i])
        
        # Initialize the max ramp width and the minimum index encountered
        max_width = 0
        min_index = float('inf')
        
        # Traverse through sorted indexes and calculate the width of ramps
        for i in sorted_indexes:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
        
        return max_width

# Example usage:
solution = Solution()
nums1 = [6, 0, 8, 2, 1, 5]
print(solution.maxWidthRamp(nums1))  # Output: 4

nums2 = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
print(solution.maxWidthRamp(nums2))  # Output: 7