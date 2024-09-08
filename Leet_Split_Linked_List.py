# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:08:49 2024

@author: priya
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):  # Use __init__ instead of _init_
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k):
        # First, count the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # Determine the size of each part
        part_size = length // k
        extra_nodes = length % k  # extra nodes to distribute in the first few parts

        parts = []
        current = head
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < extra_nodes else 0)
            
            # Split the linked list for this part
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            if current:
                next_part = current.next
                current.next = None  # Cut the list
                current = next_part
            
            parts.append(part_head)

        return parts

# Helper function to print linked list parts
def print_linked_list_parts(parts):
    for part in parts:
        values = []
        while part:
            values.append(part.val)
            part = part.next
        print(values)

# Example usage:
# Input: head = [1, 2, 3], k = 5
head = ListNode(1, ListNode(2, ListNode(3)))

# Create the solution object
solution = Solution()

# Split the list
parts = solution.splitListToParts(head, 5)
print_linked_list_parts(parts)

# Example usage 2:
# Input: head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
head = ListNode(1)
current = head
for i in range(2, 11):
    current.next = ListNode(i)
    current = current.next

# Split the list
parts = solution.splitListToParts(head, 3)
print_linked_list_parts(parts)
