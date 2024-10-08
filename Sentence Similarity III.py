# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:36:00 2024

@author: priya
"""

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        # Split both sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure words1 is the longer sentence for simplicity
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        # Compare the words from the beginning
        i = 0
        while i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Compare the words from the end
        j = 0
        while j < len(words2) and words1[-(j + 1)] == words2[-(j + 1)]:
            j += 1

        # Check if all the words of the shorter sentence are either at the beginning or at the end of the longer sentence
        return i + j >= len(words2)

# Example usage:
solution = Solution()
print(solution.areSentencesSimilar("My name is Haley", "My Haley"))  # Output: True
print(solution.areSentencesSimilar("of", "A lot of words"))          # Output: False
print(solution.areSentencesSimilar("Eating right now", "Eating"))    # Output: True