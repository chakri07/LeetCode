"""

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # inorder = left,root,right
        # preorder = root,left,right
        if len(preorder) == 0:
            return None
        
        ans_node = TreeNode(preorder[0])

        left_len = inorder.index(preorder[0])
        
        ans_node.left = self.buildTree(preorder[1:left_len+1],inorder[0:left_len])
        ans_node.right = self.buildTree(preorder[left_len+1:],inorder[left_len+1:])


        return ans_node
        