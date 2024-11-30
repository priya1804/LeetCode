# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:48:53 2024

@author: priya
"""

class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialize degree tables and adjacency list
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        adj_matrix = defaultdict(list)
        
        # Build the graph
        for src, dst in pairs:
            in_degree[dst] += 1
            out_degree[src] += 1
            adj_matrix[src].append(dst)
        
        # Start node initialization for Eulerian path or circuit
        start_node_idx = pairs[0][0]  # Default to the first node
        
        # Identify the correct start node if Eulerian path exists
        for node in adj_matrix:
            if out_degree[node] - in_degree[node] == 1:
                start_node_idx = node
                break
        
        # Helper function to find Eulerian path using Hierholzer's algorithm
        def eular_path(adjMatrix, path, cur_node):
            while adjMatrix[cur_node]:
                next_visit_node = adjMatrix[cur_node].pop()
                eular_path(adjMatrix, path, next_visit_node)
                path.append([cur_node, next_visit_node])
        
        # Record the path
        record = []
        eular_path(adj_matrix, record, start_node_idx)
        
        # Return the result as a list in reversed order
        return record[::-1]  # Explicitly reverse the result