# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:02:35 2024

@author: priya
"""

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for c in s:
            if len(ans) < 2 or ans[-1] != c or ans[-2] != c:
                ans.append(c)
        return ''.join(ans)
       
     
   
        