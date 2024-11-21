# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:19:31 2024

@author: priya
"""

class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # Initialize variables
        ans = 0
        grid = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Mark guards and walls in the grid
        for row, col in guards:
            grid[row][col] = 'G'

        for row, col in walls:
            grid[row][col] = 'W'

        # Compute the left direction
        for i in range(m):
            lastCell = 0
            for j in range(n):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    lastCell = grid[i][j]
                else:
                    left[i][j] = lastCell

        # Compute the right direction
        for i in range(m):
            lastCell = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    lastCell = grid[i][j]
                else:
                    right[i][j] = lastCell

        # Compute the upward direction
        for j in range(n):
            lastCell = 0
            for i in range(m):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    lastCell = grid[i][j]
                else:
                    up[i][j] = lastCell

        # Compute the downward direction
        for j in range(n):
            lastCell = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 'G' or grid[i][j] == 'W':
                    lastCell = grid[i][j]
                else:
                    down[i][j] = lastCell

        # Count unguarded cells
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0 and
                        left[i][j] != 'G' and
                        right[i][j] != 'G' and
                        up[i][j] != 'G' and
                        down[i][j] != 'G'):
                    ans += 1

        return ans
