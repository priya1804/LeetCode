# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:02:46 2024

@author: priya
"""

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans = []  # Initialize the result list
        j = 0  # Index for the spaces list

        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(c)

        return ''.join(ans)  # Join the list to form the final string
