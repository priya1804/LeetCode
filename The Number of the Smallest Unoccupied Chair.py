# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:57:36 2024

@author: priya
"""

import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        nextUnsatChair = 0
        emptyChairs = []
        occupied = []  # (leaving, chair)

        # Add an index to each friend's time
        for i in range(len(times)):
            times[i].append(i)

        # Sort by arrival times
        times.sort(key=lambda x: x[0])

        # Process each friend's arrival and leaving
        for arrival, leaving, i in times:
            # Free up chairs when someone leaves before or at the current arrival time
            while len(occupied) > 0 and occupied[0][0] <= arrival:
                unsatChair = heapq.heappop(occupied)[1]
                heapq.heappush(emptyChairs, unsatChair)

            # If the target friend has arrived
            if i == targetFriend:
                return emptyChairs[0] if len(emptyChairs) > 0 else nextUnsatChair

            # Assign a chair to the current friend
            if len(emptyChairs) == 0:
                heapq.heappush(occupied, (leaving, nextUnsatChair))
                nextUnsatChair += 1
            else:
                emptyChair = heapq.heappop(emptyChairs)
                heapq.heappush(occupied, (leaving, emptyChair))
