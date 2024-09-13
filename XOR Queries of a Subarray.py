# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:11:51 2024

@author: priya
"""

class Solution:
    def xorQueries(self, arr, queries):
        # Compute prefix XOR array
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        # Process each query
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefix[right])
            else:
                result.append(prefix[right] ^ prefix[left - 1])

        return result

# Example 1
arr1 = [1, 3, 4, 8]
queries1 = [[0, 1], [1, 2], [0, 3], [3, 3]]

# Instantiate the Solution class
solution = Solution()
print(solution.xorQueries(arr1, queries1))  # Output: [2, 7, 14, 8]

# Example 2
arr2 = [4, 8, 2, 10]
queries2 = [[2, 3], [1, 3], [0, 0], [0, 3]]
print(solution.xorQueries(arr2, queries2))  # Output: [8, 0, 4, 4]
