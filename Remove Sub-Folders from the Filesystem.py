# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:34:09 2024

@author: priya
"""

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        ans = []
        prev = ""

        folder.sort()

        for f in folder:
            if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
                continue
            ans.append(f)
            prev = f

        return ans
