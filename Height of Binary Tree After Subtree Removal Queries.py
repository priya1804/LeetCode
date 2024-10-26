# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:23:22 2024

@author: priya
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        # valToMaxHeight[val] := the maximum height without the node with `val`
        valToMaxHeight = {}

        # maxHeight := the maximum height without the current node `root`
        def dfs(root, depth, maxHeight):
            if not root:
                return
            valToMaxHeight[root.val] = maxHeight
            dfs(root.left, depth + 1, max(maxHeight, depth + height(root.right)))
            dfs(root.right, depth + 1, max(maxHeight, depth + height(root.left)))

        dfs(root, 0, 0)
        return [valToMaxHeight[query] for query in queries]
