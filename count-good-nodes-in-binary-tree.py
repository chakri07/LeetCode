'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

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

    def goodNodes2(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0

        def sol_rec(cur, val):
            if cur.val >= val: self.res += 1
            if cur.left: sol_rec(cur.left, max(val, cur.val))
            if cur.right: sol_rec(cur.right, max(val, cur.val))

        sol_rec(root, root.val)
        return self.res