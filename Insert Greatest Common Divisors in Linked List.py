# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:16:10 2024

@author: priya
"""

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        prevNode = None
        currNode = head
        
        while currNode:
            if prevNode:
                # Calculate GCD between prevNode and currNode
                gcd = self.greatestCommonDivisor(prevNode.val, currNode.val)
                
                # Insert a new node with the GCD value
                prevNode.next = ListNode(gcd, currNode)
                
            prevNode = currNode
            currNode = currNode.next
            
        return head

    # Function to calculate the greatest common divisor (GCD) of two numbers
    def greatestCommonDivisor(self, val1, val2):
        if val2 == 0:
            return val1
        return self.greatestCommonDivisor(val2, val1 % val2)

# Helper function to print the linked list
def printLinkedList(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example usage
head = createLinkedList([18, 6, 10, 3])
print("Original List:")
printLinkedList(head)

solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)
print("List after inserting GCD nodes:")
printLinkedList(new_head)
