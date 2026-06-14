# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # inorder = left -> root -> right 
        # pre order = root -> left -> right
        root = preorder[0]
        mid = inorder.index(root)

        root_node = TreeNode(root)
        
        root_node.left = self.buildTree(preorder[1:1+mid], inorder[0:mid])
        root_node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root_node