# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:56:23 2024

@author: priya
"""

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])  # dimensions for matrix
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:  # cell is in the first row or column
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        return ans
