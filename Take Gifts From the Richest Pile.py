# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:03:09 2024

@author: priya
"""

import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        while k > 0:
            # Find the maximum pile
            max_pile = max(gifts)
            index = gifts.index(max_pile)

            # Replace the maximum pile with its square root (floored to integer)
            gifts[index] = int(math.sqrt(max_pile))

            # Decrement the number of operations
            k -= 1

        # Return the sum of the gifts
        return sum(gifts)
