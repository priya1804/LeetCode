# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:03:20 2024

@author: priya
"""

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # 26 lowercase English letters
        self.count = 0  # Count of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.count += 1  # Increment the count for every prefix part

    def calculate_prefix_score(self, word):
        node = self.root
        prefix_score = 0
        for char in word:
            index = ord(char) - ord('a')
            node = node.children[index]
            prefix_score += node.count  # Add the count of words sharing this prefix
        return prefix_score

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the sum of prefix scores for each word
        result = []
        for word in words:
            result.append(trie.calculate_prefix_score(word))
        
        return result
