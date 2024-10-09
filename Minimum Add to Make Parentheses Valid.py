# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:42:53 2024

@author: priya
"""

class Solution {
public:
    int minAddToMakeValid(string s) {
        int l = 0, r = 0; // Variables to track left '(' and required right ')' characters

        for (char c : s) {
            if (c == '(') {
                l++;  // Increment for '('
            } else {
                if (l == 0) {
                    r++;  // No '(' to balance, so we need a right ')'
                } else {
                    l--;  // A matching '(' found, so we decrement
                }
            }
        }

        return l + r;  // Remaining unbalanced '(' + unbalanced ')'
    }
};
