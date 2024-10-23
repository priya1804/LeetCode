# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:33:30 2024

@author: priya
"""

class Solution:
    def dfs(self, node):
        if not node:
            return
        # Root will always be 0
        # Otherwise get the sum of its level minus the parent's children's sum
        if node.parent:
            node.val = self.level_sums[node.level] - node.parent.child_sum
        else:
            node.val = 0  # Root value will always be 0

        # Perform DFS traversal on the left and right children
        self.dfs(node.left)
        self.dfs(node.right)

    def replaceValueInTree(self, root):
        root.parent = None  # Root has no parent
        root.level = 0  # Root is at level 0
        queue = [root]
        self.level_sums = dict()  # Dictionary to store sum of node values at each level

        # BFS to calculate level sums and children's sum for each node
        while queue:
            node = queue.pop(0)  # Simulate BFS by popping from the front of the queue
            node.child_sum = 0  # Initialize the sum of the current node's children
            
            if node.level not in self.level_sums:
                self.level_sums[node.level] = 0  # Initialize level sum if not present
            
            self.level_sums[node.level] += node.val  # Add node's value to its level's sum

            # Process left child
            if node.left:
                node.left.parent = node  # Set parent for the left child
                node.left.level = node.level + 1  # Set level for the left child
                node.child_sum += node.left.val  # Add left child's value to the parent's child sum
                queue.append(node.left)
            
            # Process right child
            if node.right:
                node.right.parent = node  # Set parent for the right child
                node.right.level = node.level + 1  # Set level for the right child
                node.child_sum += node.right.val  # Add right child's value to the parent's child sum
                queue.append(node.right)

        # Perform DFS to update node values
        self.dfs(root)
        return root