# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:38:35 2024

@author: priya
"""

class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()
        
        # Check if the last character of each word matches the first character of the next word
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check if the first character of the first word matches the last character of the last word
        return words[0][0] == words[-1][-1]
