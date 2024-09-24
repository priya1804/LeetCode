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
        
        # Sort both arrays to group similar prefixes together
        arr1.sort()
        arr2.sort()
        
        def common_prefix_length(s1, s2):
            # Use binary search to quickly find the longest common prefix
            low, high = 0, min(len(s1), len(s2))
            
            while low < high:
                mid = (low + high + 1) // 2
                if s1[:mid] == s2[:mid]:
                    low = mid  # Increase the size of the common prefix
                else:
                    high = mid - 1  # Reduce the size of the common prefix
            return low

        # Initialize the maximum common prefix length to 0
        max_len = 0
        
        # Only compare pairs of strings from the sorted arrays
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            max_len = max(max_len, common_prefix_length(arr1[i], arr2[j]))
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
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
