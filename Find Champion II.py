# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:31:44 2024

@author: priya
"""

class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        inDegrees = [0] * n

        # Ensure this loop is indented correctly inside the method
        for _, v in edges:
            inDegrees[v] += 1

        # Return the champion node if there is exactly one node with in-degree 0
        return (-1 if inDegrees.count(0) > 1 else inDegrees.index(0))
