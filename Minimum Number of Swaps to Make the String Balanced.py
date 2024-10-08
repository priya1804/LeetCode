# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:32:41 2024

@author: priya
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0  # This variable tracks the number of imbalanced pairs

        # Iterate through each character in the string
        for c in s:
            # If the character is an opening bracket, we increment imbalance
            if c == '[':
                imbalance += 1
            # If the character is a closing bracket
            elif imbalance:
                # If there's an imbalance, we decrement it as the closing bracket balances an opening one
                imbalance -= 1

        # The minimum number of swaps is the number of unmatched open brackets divided by 2 (rounded up)
        # because each swap can fix two imbalances.
        return (imbalance + 1) // 2
