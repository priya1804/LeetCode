# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 07:56:45 2024

@author: priya
"""

from collections import deque
from itertools import tee

def pairwise(iterable):
    """Generate pairs from iterable: (s0, s1), (s1, s2), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])  # (row, col, obstacles)
        visited = set()
        directions = (-1, 0, 1, 0, -1)  # For movement: up, right, down, left

        while queue:
            i, j, obstacle_count = queue.popleft()
            
            # Check if the bottom-right corner is reached
            if i == rows - 1 and j == cols - 1:
                return obstacle_count

            if (i, j) in visited:
                continue
            visited.add((i, j))

            # Explore all four directions
            for dx, dy in pairwise(directions):
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                    if grid[x][y] == 0:
                        queue.appendleft((x, y, obstacle_count))  # No obstacle, prioritize by appending to the left
                    else:
                        queue.append((x, y, obstacle_count + 1))  # Obstacle, append to the right


