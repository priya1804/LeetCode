# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:13:31 2024

@author: priya
"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()  # Initialize an empty set to track seen numbers

        for a in arr:
            if a * 2 in seen or (a % 2 == 0 and a // 2 in seen):
                return True
            seen.add(a)

        return False
