# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:58:57 2024

@author: priya
"""

class Solution:
    def lexicalOrder(self, n):
        ans = []
        curr = 1
        
        while len(ans) < n:
            ans.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr == n:
                    curr //= 10
                curr += 1
        
        return ans
