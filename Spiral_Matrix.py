# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:57:39 2024

@author: priya
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m, n, head):
        # Initialize the matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Directions for spiral traversal: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        
        row, col = 0, 0  # Start at the top-left corner
        current = head
        for _ in range(m * n):
            if current:
                matrix[row][col] = current.val
                current = current.next
            else:
                break

            # Try to move in the current direction
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]

            # If out of bounds or the cell is already filled, change direction
            if not (0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1):
                direction_idx = (direction_idx + 1) % 4  # Change direction
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]

            # Move to the next cell
            row, col = next_row, next_col
        
        return matrix

# Helper function to create a linked list from a list
def createLinkedList(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
m = 3
n = 5
linked_list = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
head = createLinkedList(linked_list)

# Create a Solution object and call the spiralMatrix method
solution = Solution()
result = solution.spiralMatrix(m, n, head)

for row in result:
    print(row)
