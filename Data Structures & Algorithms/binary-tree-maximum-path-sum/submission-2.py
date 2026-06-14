# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(node,ans):
            print(ans)
            if not node:
                return 0
            print("p")
            print(node.val)
            left_max = max(helper(node.left,ans),0)
            right_max = max(helper(node.right,ans),0)

            ans[0] = max(left_max + right_max + node.val, ans[0])

            return max(left_max,right_max) + node.val

        ans = [float('-inf')]
        helper(root,ans)
         
        return ans[0]