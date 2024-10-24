# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:52:43 2024

@author: priya
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1:  # This is the first condition
            return not root2  # Correctly indented

        if not root2:  # Second condition to check
            return not root1  # Correctly indented

        if root1.val != root2.val:  # Check if values are equal
            return False  # Return False if values are not equal

        # Recursive calls to check the structure of the subtrees
        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
