"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        # creates a brand new empty list whenever no neighbors were supplied.
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        start = node

        old_to_new = {}
        stck =[node]
        visited = set()
        visited.add(start)

        #iterative dfs
        while stck:
            node = stck.pop()
            old_to_new[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stck.append(nei)

        for old_node,new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei = old_to_new[nei]
                new_node.neighbors.append(new_nei)

        return old_to_new[start]
            

