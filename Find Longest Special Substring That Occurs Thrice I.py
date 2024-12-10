# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:40:13 2024

@author: priya
"""

class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        freq = defaultdict(int)
        substrings = [''.join(s) for _, s in groupby(s)]
        for s in substrings:
            n = len(s)
            freq[s] += 1
            if freq[s] == 3:
                res = max(res, n)
            else:
                if n > 1:
                    t = s[1:]
                    freq[t] += 2
                    if freq[t] >= 3:
                        res = max(res, n - 1)
                if n > 2:
                    res = max(res, n - 2)
        return res