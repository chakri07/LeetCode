"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = collections.defaultdict(list)

        def build_graph_from_tree(curr,parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            
            if curr.left:
                build_graph_from_tree(curr.left, curr)
            if curr.right:
                build_graph_from_tree(curr.right, curr)

        build_graph_from_tree(root, None)
        ans = []
        visited = set([target.val])

        def dfs(node, distance):
            if distance == k:
                ans.append(node)
                return 
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour, distance + 1)

        dfs(target.val,0)
        return ans
