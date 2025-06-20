"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

 

Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.


https://leetcode.com/problems/longest-path-with-different-adjacent-characters
"""

from collections import defaultdict
from typing import List

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        
        # 1. Build the graph (adjacency list)
        graph = defaultdict(list)
        for i in range(1, n): # Start from 1, as parent[0] is -1 (root's parent)
            graph[parent[i]].append(i)

        # Initialize the global maximum path length.
        # A single node itself is a path of length 1.
        self.max_path_length = 1 

        # 2. DFS function
        # This function returns the length of the longest valid path
        # starting at 'node' and going downwards into one of its children.
        # This path must have all adjacent characters different.
        def dfs(node: int) -> int:
            # max_arm_from_node represents the longest path starting at 'node'
            # and going downwards, where adjacent characters are different.
            # It's initialized to 1 because the node itself contributes a length of 1.
            max_arm_from_node = 1 
            
            # To find the two longest arms (paths) extending downwards from 'node'
            # (only considering paths with different adjacent characters).
            # These two arms can potentially be combined to form the global max_path_length.
            longest_child_arm = 0
            second_longest_child_arm = 0

            # Iterate over children of the current node
            for child in graph[node]:
                # Recursively call DFS for the child.
                # child_path_len is the longest path starting at 'child' going downwards.
                child_path_len = dfs(child)
                
                # Check if we can extend a path from 'node' to 'child'
                # (i.e., characters are different)
                if s[node] != s[child]:
                    if child_path_len > longest_child_arm:
                        second_longest_child_arm = longest_child_arm
                        longest_child_arm = child_path_len
                    elif child_path_len > second_longest_child_arm:
                        second_longest_child_arm = child_path_len
            
            self.max_path_length = max(self.max_path_length, longest_child_arm + second_longest_child_arm + 1)

            return longest_child_arm + 1

        # Start DFS from the root (node 0)
        dfs(0) 
        
        return self.max_path_length