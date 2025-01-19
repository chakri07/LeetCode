'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false




Link: https://leetcode.com/problems/subtree-of-another-tree
'''
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return False
        if not root:
            return False
        if self.isEqual(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def isEqual(self, root1:TreeNode,root2:TreeNode):
        if (not root1) and (not root2):
            return True
        elif root1 and not root2:
            return False
        elif not root1 and root2:
            return False
        else :
            if root1.val == root2.val:
                left = self.isEqual(root1.left,root2.left)
                right = self.isEqual(root1.right,root2.right)
                return left and right
            else:
                return False
            

## Slightly modified 

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        def equal(node1,node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            return node1.val == node2.val and \
                equal(node1.right,node2.right) and \
                equal(node1.left,node2.left)
                
        return equal(root,subRoot) or \
            self.isSubtree(root.left,subRoot) or \
            self.isSubtree(root.right,subRoot)
            