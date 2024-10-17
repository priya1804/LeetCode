# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:11:19 2024

@author: priya
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        # Dictionary to store the last occurrence of each digit
        digit_last_pos = {c: i for i, c in enumerate(s)}
        
        # Traverse through each digit of the number
        for i, c in enumerate(s):
            # Check if there's a larger digit that appears later
            for digit in reversed('0123456789'):
                if digit <= c:
                    break
                if digit in digit_last_pos and digit_last_pos[digit] > i:
                    # Swap the digits
                    s[i], s[digit_last_pos[digit]] = s[digit_last_pos[digit]], s[i]
                    # Convert list back to integer and return
                    return int(''.join(s))
        
        # If no swap is done, return the original number
        return num
