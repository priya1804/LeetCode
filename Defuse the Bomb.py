# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:48:42 2024

@author: priya
"""

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans

        summ = 0
        start = 1 if k > 0 else n + k  # the start of the next k numbers
        end = k if k > 0 else n - 1  # the end of the next k numbers

        for i in range(start, end + 1):
            summ += code[i % n]

        for i in range(n):
            ans[i] = summ
            summ -= code[start % n]
            start += 1
            end += 1
            summ += code[end % n]

        return ans
