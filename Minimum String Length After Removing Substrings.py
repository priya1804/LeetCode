# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:36:26 2024

@author: priya
"""

class Solution:
    def minLength(self, s):
        stack = []
        
        # Iterate through the string
        for char in s:
            # If the last two characters in the stack form "AB" or "CD", remove them
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()
            else:
                stack.append(char)
        
        # The length of the remaining stack is the minimum possible length
        return len(stack)

# Test cases
s1 = "ABFCACDB"
s2 = "ACBBD"

# Creating an instance of Solution
solution = Solution()

# Calling the method with the test cases
print(solution.minLength(s1))  # Output: 2
print(solution.minLength(s2))  # Output: 5