"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        def get_graph_from_root(node,parent):
            if not node:
                return

            if parent:
                graph[node.val].append((parent,'U'))
            
            if node.left:
                graph[node.val].append((node.left,'L'))
                get_graph_from_root(node.left, node)
            
            if node.right:
                graph[node.val].append((node.right,'R'))
                get_graph_from_root(node.right, node)
        
        if not root:
            return 
        
        get_graph_from_root(root,None)
        
        queue = deque([(startValue,'')])
        visited = set()


        while queue:
            node_val, path = queue.popleft()
            
            if node_val == destValue:
                return path
            
            for n, direc in graph[node_val]:
                if n.val not in visited:
                    visited.add(n.val)
                    queue.append((n.val, path + direc))

        return ''