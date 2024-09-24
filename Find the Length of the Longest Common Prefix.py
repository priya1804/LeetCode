# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:55:27 2024

@author: priya
"""

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # Convert all integers to string for easier prefix comparison
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        
        def common_prefix_length(s1, s2):
            # Find the length of the common prefix between two strings
            length = 0
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    length += 1
                else:
                    break
            return length

        # Initialize the maximum common prefix length to 0
        max_len = 0
        
        # Compare each pair of strings from arr1 and arr2
        for num1 in arr1:
            for num2 in arr2:
                max_len = max(max_len, common_prefix_length(num1, num2))
        
        return max_len

# Example usage:
solution = Solution()

# Test case 1:
arr1 = [1, 10, 100]
arr2 = [1000]
print(solution.longestCommonPrefix(arr1, arr2))  # Output: 3

# Test case 2:
arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(solution.longestCommonPrefix(arr1, arr2))  # Output: 0
