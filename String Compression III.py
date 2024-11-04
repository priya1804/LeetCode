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
        n = len(s)
        res = []
        count = 1
        letter = s[0]
        for i in range(1, n):
            if s[i] != s[i-1] or count >= 9:
                res.append(str(count))
                res.append(letter)
                count = 0
            count += 1
            letter = s[i]
        res.append(str(count))
        res.append(letter)
        return ''.join(res)
