"""

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
Example 2:


Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).


https://leetcode.com/problems/longest-univalue-path/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]
        if not root:
            return 0

        def helper(node):
            if not node:
                return 0
            
            left_len = 0 
            right_len = 0 

            left = helper(node.left)
            right = helper(node.right)

            if node.left and node.left.val == node.val:
                left_len = left + 1

            if node.right and node.right.val == node.val:
                right_len = right + 1

            ans[0] = max(ans[0], left_len + right_len)

            return max(left_len, right_len)

        helper(root)
        return ans[0]
