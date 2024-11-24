# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:18:31 2024

@author: priya
"""

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        absSum = 0
        minAbs = float('inf')  # Initialize to a very large number
        oddNeg = 0  # Tracks whether the count of negative numbers is odd

        for row in matrix:
            for num in row:
                absSum += abs(num)  # Add the absolute value
                minAbs = min(minAbs, abs(num))  # Track the smallest absolute value
                if num < 0:
                    oddNeg ^= 1  # Toggle odd/even state for negative numbers

        # If oddNeg is 1 (odd negatives), subtract twice the smallest absolute value
        return absSum - oddNeg * minAbs * 2

