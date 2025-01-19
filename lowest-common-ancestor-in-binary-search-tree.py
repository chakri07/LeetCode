"""
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
Example 2:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root : 
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
            
