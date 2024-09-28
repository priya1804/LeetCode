# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:44:55 2024

@author: priya
"""

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        self.head = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        tail_index = (self.head + self.size) % self.capacity
        self.queue[tail_index] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        tail_index = (self.head + self.size - 1) % self.capacity
        return self.queue[tail_index]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity
