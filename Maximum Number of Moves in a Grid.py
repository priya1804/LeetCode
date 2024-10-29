# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:27:53 2024

@author: priya
"""

class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
          # Define the directions in which to move (up-right, right, down-right)
        directions = ((-1, 1), (0, 1), (1, 1))
      
        # Get the dimensions of the grid
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Initialize a queue with all possible starting positions in the first column
        queue = deque((row, 0) for row in range(num_rows))
      
        # Initialize a 2D list to keep track of the distance for each cell
        distance = [[0] * num_cols for _ in range(num_rows)]
      
        # Initialize the maximum number of moves to 0
        max_moves = 0
      
        # Iterate through the queue until it is empty
        while queue:
            # Pop the current cell from the queue
            i, j = queue.popleft()
          
            # Iterate through the possible directions
            for delta_row, delta_col in directions:
                # Calculate the new coordinates
                new_row, new_col = i + delta_row, j + delta_col
              
                # Check if the new position is within bounds
                # and if moving there increases the distance
                if (0 <= new_row < num_rows and
                    0 <= new_col < num_cols and
                    grid[new_row][new_col] > grid[i][j] and
                    distance[new_row][new_col] < distance[i][j] + 1):
                  
                    # Update the distance for the new cell
                    distance[new_row][new_col] = distance[i][j] + 1
                  
                    # Update the maximum number of moves
                    max_moves = max(max_moves, distance[new_row][new_col])
                  
                    # Add the new cell to the queue
                    queue.append((new_row, new_col))
      
        # Return the maximum number of moves
        return max_moves        