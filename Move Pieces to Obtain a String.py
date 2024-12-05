# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:38:56 2024

@author: priya
"""

class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i = 0  # start's index
        j = 0  # target's index

        while i < n and j < n:
            # Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            # Skip underscores in target
            while j < n and target[j] == '_':
                j += 1

            # If one reaches the end and the other doesn't
            if i == n or j == n:
                break

            # If characters do not match
            if start[i] != target[j]:
                return False

            # R can only move right, L can only move left
            if (start[i] == 'R' and i > j) or (start[i] == 'L' and i < j):
                return False

            i += 1
            j += 1

        # Check remaining characters are underscores in both strings
        while i < n:
            if start[i] != '_':
                return False
            i += 1
        while j < n:
            if target[j] != '_':
                return False
            j += 1

        return True
