# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:56:20 2024

@author: priya
"""

import heapq

class Solution(object):
    def smallestRange(self, nums):
        # Create a min heap and initialize it with the first element from each row.
        minHeap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(minHeap)

        # Initialize the maximum value in the current range
        maxRange = max(row[0] for row in nums)
        # Get the smallest element from the heap (initial minRange)
        minRange = heapq.nsmallest(1, minHeap)[0][0]
        ans = [minRange, maxRange]

        # Iterate while the heap contains one element from each list
        while len(minHeap) == len(nums):
            num, r, c = heapq.heappop(minHeap)
            
            # If there are more elements in the current row, push the next element to the heap
            if c + 1 < len(nums[r]):
                heapq.heappush(minHeap, (nums[r][c + 1], r, c + 1))
                maxRange = max(maxRange, nums[r][c + 1])
                minRange = heapq.nsmallest(1, minHeap)[0][0]
                
                # Update the answer if the current range is smaller
                if maxRange - minRange < ans[1] - ans[0]:
                    ans[0], ans[1] = minRange, maxRange
        
        return ans
