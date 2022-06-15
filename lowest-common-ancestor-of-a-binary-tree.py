'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q,{})
        
    
    def helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode',dp) -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        if self.isContains(root.left,p,dp) and self.isContains(root.left,q,dp):
            return self.helper(root.left,p,q,dp)
        if self.isContains(root.right,p,dp) and self.isContains(root.right,q,dp):
            return self.helper(root.right,p,q,dp)
        return root
        
    def isContains(self,root,node,dp):
        if (root,node) in dp:
            return dp[(root,node)]
        if not root:
            return False
        if root == node:
            return True
        ans = self.isContains(root.left,node,dp) or self.isContains(root.right,node,dp)
        dp[(root,node)] = ans
        return ans
        
# recursion approach
class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans