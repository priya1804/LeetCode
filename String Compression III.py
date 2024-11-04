# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:17:55 2024

@author: priya
"""

class Solution(object):
    def compressedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        comp = ""
        n = len(s)
        i = 0

        while i < n:
            ch = s[i]
            cnt = 0
            while i < n and s[i] == ch and cnt < 9:
                cnt += 1
                i += 1
            comp += str(cnt) + ch
        return comp