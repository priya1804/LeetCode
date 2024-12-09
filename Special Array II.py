# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:35:38 2024

@author: priya
"""

class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        store, ans = [], []

        for i in range(1, n):
            if (nums[i] % 2) == (nums[i - 1] % 2):
                store.append(i)

        for left, right in queries:
            idx = bisect_right(store, left)
            
            if idx < len(store) and store[idx] <= right: ans.append(False)
            else: ans.append(True)
        
        return ans