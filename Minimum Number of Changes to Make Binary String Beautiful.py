# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:31:28 2024

@author: priya
"""

class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(a != b for a, b in zip(s[::2], s[1::2]))
        