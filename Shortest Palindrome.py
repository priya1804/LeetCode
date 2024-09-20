# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:22:56 2024

@author: priya
"""

class Solution:
    def shortestPalindrome(self, s):
        # Create a new string which is the original string + '#' + reverse of the string
        # The '#' acts as a separator to avoid overlap.
        rev_s = s[::-1]
        new_s = s + '#' + rev_s

        # KMP table to store the longest prefix suffix values
        n = len(new_s)
        lps = [0] * n

        # Build the LPS array for the new string
        for i in range(1, n):
            length = lps[i - 1]
            while length > 0 and new_s[i] != new_s[length]:
                length = lps[length - 1]
            if new_s[i] == new_s[length]:
                length += 1
            lps[i] = length

        # The last value in lps will tell us the length of the longest palindromic prefix
        to_add = rev_s[:len(s) - lps[-1]]

        return to_add + s

# Example usage
s1 = "aacecaaa"
sol = Solution()
print(sol.shortestPalindrome(s1))  # Output: "aaacecaaa"

s2 = "abcd"
print(sol.shortestPalindrome(s2))  # Output: "dcbabcd"
