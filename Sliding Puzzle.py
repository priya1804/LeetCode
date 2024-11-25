# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:42:42 2024

@author: priya
"""

from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # Target state
        target = "123450"
        
        # Convert the board into a single string representation
        start = ''.join(str(num) for row in board for num in row)
        
        # Neighbor positions for swapping based on a 2x3 board
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        # BFS initialization
        queue = deque([(start, 0)])  # (current_state, move_count)
        seen = set()  # To track visited states
        seen.add(start)
        
        while queue:
            state, moves = queue.popleft()
            
            # If the current state matches the target, return the number of moves
            if state == target:
                return moves
            
            # Find the index of the empty tile (0)
            zero_pos = state.index('0')
            
            # Generate new states by swapping the empty tile with its neighbors
            for neighbor in neighbors[zero_pos]:
                state_list = list(state)
                state_list[zero_pos], state_list[neighbor] = state_list[neighbor], state_list[zero_pos]
                next_state = ''.join(state_list)
                
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, moves + 1))
        
        # If we exhaust the queue and never reach the target, return -1
        return -1
