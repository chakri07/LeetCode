"""
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []

https://neetcode.io/problems/level-order-traversal-of-binary-tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        level = []
        child_queue = []

        while queue:
            node = queue[0]
            level.append(node.val)
            queue.remove(node)
            if node.left:
                child_queue.append(node.left) 
            if node.right:
                child_queue.append(node.right) 
            if len(queue) == 0:
                queue = child_queue
                child_queue = []
                ans.append(level)
                level = []

        return ans
                
