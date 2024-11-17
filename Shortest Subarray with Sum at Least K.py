# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:04:02 2024

@author: priya
"""

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Custom accumulate to handle versions without the 'initial' argument
        def custom_accumulate(iterable):
            total = 0
            yield total  # This serves as the 'initial' value
            for value in iterable:
                total += value
                yield total

        n = len(nums)
        ans = n + 1
        dq = collections.deque()
        prefix = list(custom_accumulate(nums))

        for i in range(n + 1):
            # Check if the current subarray satisfies the condition
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            
            # Maintain the deque in increasing order of prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)

        return ans if ans <= n else -1
