# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:18:20 2024

@author: priya
"""

import string

class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i = 0  # Index for str2

        for c in str1:
            if i < len(str2) and (c == str2[i] or chr((ord(c) - ord('a') + 1) % 26 + ord('a')) == str2[i]):
                i += 1
            if i == len(str2):
                return True

        return False
