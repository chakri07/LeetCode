'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

https://leetcode.com/problems/binary-tree-level-order-traversal/
'''


# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = collections.defaultdict(list)
        self.helper(root,0,ans)
        return list(ans.values())
          
    def helper(self,root,level,ans):
        if not root:
            return
        if level in ans:
            ans[level].append(root.val)
        else:
            ans[level] = [root.val]
            
    
        self.helper(root.left,level+1,ans)
        self.helper(root.right,level+1,ans)