# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:20:29 2024

@author: priya
"""

import heapq

class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Check for the initial impossible case where the immediate neighbors of the start are too high
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        inf = float('inf')  # Use float('inf') for Python 2.x

        # Initialize distance matrix with infinity
        distance = [[inf] * cols for _ in range(rows)]
        distance[0][0] = 0  # Start point has distance 0

        # Priority queue for the BFS: (time, row, col)
        priority_queue = [(0, 0, 0)]
        heapq.heapify(priority_queue)

        # Directions for exploring neighbors (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Explore the grid until we reach the bottom-right corner
        while priority_queue:
            time, row, col = heapq.heappop(priority_queue)

            # If we reached the end, return the distance
            if row == rows - 1 and col == cols - 1:
                return time

            # Check all neighboring squares
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_time = time + 1  # Increment time by one step

                    # Ensure to wait if arriving too early
                    if new_time < grid[new_row][new_col]:
                        wait_time = (grid[new_row][new_col] - new_time) % 2
                        new_time = grid[new_row][new_col] + wait_time

                    # If this path is faster, update the distance and push to the queue
                    if new_time < distance[new_row][new_col]:
                        distance[new_row][new_col] = new_time
                        heapq.heappush(priority_queue, (new_time, new_row, new_col))

        # If we never reached the end, return -1
        return -1
