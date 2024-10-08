# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:36:39 2024

@author: priya
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        # Get the length of both strings
        len_s1, len_s2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len_s1 > len_s2:
            return False
        
        # Count the frequency of characters in s1
        s1_count = Counter(s1)
        # Create a window with the first len_s1 characters of s2
        window_count = Counter(s2[:len_s1])
        
        # If the initial window matches, return True
        if s1_count == window_count:
            return True
        
        # Use a sliding window approach to move through s2
        for i in range(len_s1, len_s2):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s2[i - len_s1]] -= 1
            
            # Clean up the dictionary by removing entries with zero counts
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Check if the current window matches the s1 count
            if window_count == s1_count:
                return True
        
        return False

# Example usage in a platform
# s1 = "ab"
# s2 = "eidbaooo"
# print(Solution().checkInclusion(s1, s2))  # Output: True
