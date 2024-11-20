# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:32:23 2024

@author: priya
"""

class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Count the frequency of each character in the string s
        char_count = Counter(s)
      
        # Check if the count of any character 'a', 'b', or 'c' is less than k
        if any(char_count[char] < k for char in "abc"):
            return -1  # If so, return -1 as we cannot fulfill the requirement
      
        # Initialize answer and the start index to 0
        max_length = start_index = 0
      
        # Iterate over the string with index i and character c
        for i, c in enumerate(s):
            char_count[c] -= 1  # Decrement the count of the current character
          
            # If count of current character is less than k, move the start index forward
            # to find a valid substring
            while char_count[c] < k:
                char_count[s[start_index]] += 1  # Increment the character at start index
                start_index += 1  # Move the start index forward
          
            # Update max_length to the maximum length found so far
            max_length = max(max_length, i - start_index + 1)
      
        # Return the length of the string minus the maximum length of a valid substring
        return len(s) - max_length
