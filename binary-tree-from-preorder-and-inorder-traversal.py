"""

Construct Binary Tree from Preorder and Inorder Traversal
Solved 
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000

https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
"""

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # inorder = left -> root -> right 
        # pre order = root -> left -> right
        root = preorder[0]
        mid = inorder.index(root)
        # so left tree will be everything before root in inorder list
        # so right tree will be everything before root in inorder list

        # In pre order left will be 1st to len(left inorder) which is mid
        # and remaining is right

        root_node = TreeNode(root)
        
        root_node.left = self.buildTree(preorder[1:1+mid], inorder[0:mid])
        root_node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root_node