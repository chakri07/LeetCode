"""

Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.

Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

 

Example 1:


Input: root = [1,3,2], k = 1
Output: 2
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:


Input: root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.
Example 3:


Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Output: 3
Explanation: The leaf node with value 3 (and not the lea

https://leetcode.com/problems/closest-leaf-in-a-binary-tree
"""

from collections import defaultdict, deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # Graph will store TreeNode objects as keys and lists of TreeNode objects as values
        graph = defaultdict(list)
        # To find the starting node (TreeNode object) for BFS
        start_node = None

        def make_graph(parent, node):
            nonlocal start_node
            if not node:
                return

            if node.val == k:
                start_node = node

            if parent:
                graph[node].append(parent)
                graph[parent].append(node) # Bidirectional edge

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node) # Bidirectional edge
                make_graph(node, node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node) # Bidirectional edge
                make_graph(node, node.right)

        make_graph(None, root)

        # Handle the case where k is the root and the root is also a leaf
        if not root.left and not root.right and root.val == k:
            return root.val

        queue = deque([(start_node, 0)])
        visited = set()
        visited.add(start_node)

        while queue:
            curr_node, curr_dist = queue.popleft()

            # Check if curr_node is a leaf
            # A node is a leaf if it has no children (left and right are None)
            # And it must be considered a leaf if it was initially the only node in the tree
            # For the general case, we check if it has children in the tree structure
            # (which is better than relying on the graph which also includes parent links)
            if not curr_node.left and not curr_node.right:
                return curr_node.val

            for neigh in graph[curr_node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, curr_dist + 1))

        return -1 # Should not be reached if k is guaranteed to be in the tree and a leaf exists