# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:12:32 2024

@author: priya
"""

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []
        
    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True