'''

https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            return self.helper(root,float('-inf'))
            
    def helper(self, root: TreeNode,max_val)->int:
        if root == None:
            return 0 
        if max_val > root.val:
            return self.helper(root.left,max_val) + self.helper(root.right,max_val)
        else:
            return self.helper(root.left,root.val) + self.helper(root.right,root.val)+1