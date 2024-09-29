# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:23:39 2024

@author: priya
"""

class Node:
    def __init__(self, count, key=None):
        self.count = count
        self.keys = {key} if key else set()
        self.prev = None
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.count == other.count and self.keys == other.keys


class AllOne(object):

    def __init__(self):
        self.keyToNode = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key):
        """
        Increments the frequency of the key by 1. Adds the key if it does not exist.
        :type key: str
        :rtype: None
        """
        if key in self.keyToNode:
            self._incrementExistingKey(key)
        else:
            self._addNewKey(key)

    def dec(self, key):
        """
        Decrements the frequency of the key by 1. Removes the key if its count becomes 0.
        :type key: str
        :rtype: None
        """
        self._decrementExistingKey(key)

    def getMaxKey(self):
        """
        Returns one of the keys with the maximal frequency.
        :rtype: str
        """
        return '' if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        Returns one of the keys with the minimal frequency.
        :rtype: str
        """
        return '' if self.head.next == self.tail else next(iter(self.head.next.keys))

    def _addNewKey(self, key):
        """Helper function to add a new key with frequency 1."""
        if self.head.next.count == 1:
            self.head.next.keys.add(key)
        else:
            self._insertAfter(self.head, Node(1, key))
        self.keyToNode[key] = self.head.next

    def _incrementExistingKey(self, key):
        """Helper function to increment the frequency of an existing key."""
        node = self.keyToNode[key]
        node.keys.remove(key)
        if node.next == self.tail or node.next.count > node.count + 1:
            self._insertAfter(node, Node(node.count + 1))
        node.next.keys.add(key)
        self.keyToNode[key] = node.next
        if not node.keys:
            self._remove(node)

    def _decrementExistingKey(self, key):
        """Helper function to decrement the frequency of an existing key."""
        node = self.keyToNode[key]
        node.keys.remove(key)
        if node.count > 1:
            if node.prev == self.head or node.prev.count != node.count - 1:
                self._insertAfter(node.prev, Node(node.count - 1))
            node.prev.keys.add(key)
            self.keyToNode[key] = node.prev
        else:
            del self.keyToNode[key]
        if not node.keys:
            self._remove(node)

    def _insertAfter(self, node, newNode):
        """Helper function to insert a new node after a given node."""
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode

    def _remove(self, node):
        """Helper function to remove a node."""
        node.prev.next = node.next
        node.next.prev = node.prev


# Example usage:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
