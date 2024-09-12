# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:29:04 2024

@author: priya
"""

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        consistent_count = 0  
        
        for word in words:
            consistent = True  
            
            for char in word:
                if char not in allowed: 
                    consistent = False
                    break
            
            if consistent:
                consistent_count += 1  
                
        return consistent_count  
