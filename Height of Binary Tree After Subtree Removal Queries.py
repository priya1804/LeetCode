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
        
        # Step 1: Compute height of each node and store in height_map
        height_map = {}
        def compute_height(node):
            if not node:
                return 0
            left_height = compute_height(node.left)
            right_height = compute_height(node.right)
            height_map[node.val] = 1 + max(left_height, right_height)
            return height_map[node.val]
        
        compute_height(root)
        
        # Step 2: Perform DFS to compute maximum height excluding each node
        val_to_max_height = {}
        
        def dfs(node, depth, max_height_without_node):
            if not node:
                return
            val_to_max_height[node.val] = max_height_without_node
            # Check if left and right children exist before accessing their heights
            left_max_height = max(
                max_height_without_node,
                depth + (height_map[node.right.val] if node.right else 0)
            )
            right_max_height = max(
                max_height_without_node,
                depth + (height_map[node.left.val] if node.left else 0)
            )
            dfs(node.left, depth + 1, left_max_height)
            dfs(node.right, depth + 1, right_max_height)

        dfs(root, 0, 0)
        
        # Step 3: Answer each query by fetching precomputed max height without the queried node
        return [val_to_max_height[query] for query in queries]
