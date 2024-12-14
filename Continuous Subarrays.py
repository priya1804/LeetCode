# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:59:14 2024

@author: priya
"""

from collections import deque

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        result = 0
        max_deque = deque()  # Monotonic decreasing deque for max values
        min_deque = deque()  # Monotonic increasing deque for min values

        for right in range(n):
            # Maintain the max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain the min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Adjust the window when the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Add all valid subarrays ending at `right`
            result += (right - left + 1)

        return result
