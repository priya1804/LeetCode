# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:25:37 2024

@author: priya
"""

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return len(s) == len(goal) and goal in s + s