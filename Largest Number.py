# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:28:37 2024

@author: priya
"""

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Custom comparator function
        def compare(x, y):
            return (x + y > y + x) - (x + y < y + x)
        
        # Convert numbers to strings and sort using custom comparator
        nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        
        # Join the sorted array into a single string and handle edge case for leading zeros
        result = ''.join(nums)
        
        return '0' if result[0] == '0' else result

# Example usage:
solution = Solution()

nums1 = [10, 2]
nums2 = [3, 30, 34, 5, 9]

print(solution.largestNumber(nums1))  # Output: "210"
print(solution.largestNumber(nums2))  # Output: "9534330"
