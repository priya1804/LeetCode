# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:00:19 2024

@author: priya
"""

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def backtrack(start_index, unique_count, max_unique_splits):
            # Base case: when we reach the end of the string
            if start_index == len(s):
                max_unique_splits[0] = max(max_unique_splits[0], unique_count)
                return
            
            # Explore all possible substrings starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                substring = s[start_index:end_index]
                if substring not in seen_substrings:
                    seen_substrings.add(substring)
                    backtrack(end_index, unique_count + 1, max_unique_splits)
                    seen_substrings.remove(substring)  # Backtrack
        
        seen_substrings = set()
        max_unique_splits = [0]  # Using list to store max_unique_splits
        backtrack(0, 0, max_unique_splits)
        return max_unique_splits[0]
