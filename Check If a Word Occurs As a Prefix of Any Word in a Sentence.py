# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:22:34 2024

@author: priya
"""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()

        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1
