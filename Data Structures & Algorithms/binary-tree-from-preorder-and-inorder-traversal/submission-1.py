# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # in-order = left, root, right 
        # pre-order = root, left , right .? 

        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])


        root = preorder[0]
        root_idx = -1
        for idx,num in enumerate(inorder):
            if num == root:
                root_idx = idx
                break
        
        left_inorder = inorder[:root_idx]
        left_preorder = preorder[1:1+root_idx]
        root = TreeNode(root)
        right_inorder = inorder[root_idx+1:]
        right_preorder = preorder[1+root_idx:]

        root.left = self.buildTree(left_preorder,   left_inorder)
        root.right = self.buildTree(right_preorder,   right_inorder)

        return root




