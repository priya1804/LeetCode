# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:19:34 2024

@author: priya
"""

from sortedcontainers import SortedDict
class MyCalendar:
    def __init__(self):
        self.calendar = SortedDict({float('inf'):float('inf')})     

    def book(self, start, end):
        ix = self.calendar.bisect_right(start)
        k,v = self.calendar.peekitem(ix)
        res = end <= v
        if res: self.calendar[end] = start
        return res