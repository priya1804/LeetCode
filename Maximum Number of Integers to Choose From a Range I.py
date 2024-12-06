# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:21:37 2024

@author: priya
"""

class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        # Create a set for fast lookups
        banned_set = set(banned)
        
        # Filter out banned numbers and sort the remaining ones
        valid_numbers = [i for i in range(1, n + 1) if i not in banned_set]
        
        # Initialize variables
        current_sum = 0
        count = 0
        
        # Iterate through valid numbers
        for num in valid_numbers:
            if current_sum + num <= maxSum:
                current_sum += num
                count += 1
            else:
                break
        
        return count
