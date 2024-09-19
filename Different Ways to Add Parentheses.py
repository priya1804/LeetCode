# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:51:37 2024

@author: priya
"""

class Solution:
    def __init__(self):
        self.memo = {}

    def diffWaysToCompute(self, expression):
        if expression in self.memo:
            return self.memo[expression]
        
        ans = []

        for i, c in enumerate(expression):
            if c in '+-*':
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])
                
                for a in left_results:
                    for b in right_results:
                        if c == '+':
                            ans.append(a + b)
                        elif c == '-':
                            ans.append(a - b)
                        elif c == '*':
                            ans.append(a * b)
        
        if not ans:
            ans = [int(expression)]
        
        self.memo[expression] = ans
        return ans
