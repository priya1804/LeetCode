# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 07:45:53 2024

@author: priya
"""

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Sort the list of numbers to leverage binary search advantage.
        nums.sort()
      
        fair_pairs_count = 0
      
        # Iterate over each number to find suitable pairs.
        for index, num in enumerate(nums):
            # Find the left boundary for fair pairs.
            left_index = bisect_left(nums, lower - num, lo=index + 1)
            # Find the right boundary for fair pairs.
            right_index = bisect_left(nums, upper - num + 1, lo=index + 1)
          
            # Update the count of fair pairs by the number of elements that
            # fall between the calculated left and right boundaries.
            fair_pairs_count += right_index - left_index
      
        # Return the total number of fair pairs.
        return fair_pairs_count
        