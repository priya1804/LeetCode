# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:58:32 2024

@author: priya
"""

class Solution:
    def longestSubarray(self, nums):
        # Find the maximum element in the array
        max_val = max(nums)
        
        # Variables to track the current length and the maximum length
        current_length = 0
        max_length = 0
        
        # Iterate through the array
        for num in nums:
            if num == max_val:
                # If the current number is equal to the maximum value, extend the current subarray
                current_length += 1
                # Update the max_length if needed
                max_length = max(max_length, current_length)
            else:
                # Reset the current length when the number is not equal to max_val
                current_length = 0
        
        return max_length

# Example usage:
nums1 = [1, 2, 3, 3, 2, 2]
sol = Solution()
print(sol.longestSubarray(nums1))  # Output: 2

nums2 = [1, 2, 3, 4]
print(sol.longestSubarray(nums2))  # Output: 1