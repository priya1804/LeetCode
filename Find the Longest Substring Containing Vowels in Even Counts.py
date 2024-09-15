# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:39:26 2024

@author: priya
"""

class Solution:
    def findTheLongestSubstring(self, s):
        # Vowel to bitmask index mapping
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        # Bitmask to track the first occurrence of a particular bitmask
        state_to_index = {0: -1}
        state = 0  # This is the bitmask to track even/odd counts of vowels
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                # Flip the bit corresponding to the vowel in the bitmask
                state ^= (1 << vowels[char])

            # If this state has been seen before, we have a valid substring
            if state in state_to_index:
                max_length = max(max_length, i - state_to_index[state])
            else:
                # Record the first occurrence of this state
                state_to_index[state] = i

        return max_length