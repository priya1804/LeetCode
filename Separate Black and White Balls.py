# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:44:07 2024

@author: priya
"""

class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Length of the given string
        length = len(s)

        # Initialize 'answer' for holding the minimum steps and
        # 'one_count' for keeping track of the number of '1's encountered
        answer = 0
        one_count = 0

        # Traverse the string in reverse from last to first character
        for i in reversed(range(length)):
            # Check if the current character is '1'
            if s[i] == '1':
                # If it's '1', increment the 'one_count'
                one_count += 1
                # Update answer by how many steps needed to move this '1' to the end
                # considering the number of ones already counted.
                answer += (length - i - 1) - one_count + 1

        # Return the total minimum steps calculated
        return answer       