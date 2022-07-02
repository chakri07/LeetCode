'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]

https://leetcode.com/problems/find-leaves-of-binary-tree/
'''

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = collections.defaultdict(list)
        self.getHeight(root,ans)
        return ans.values()
    
    def getHeight(self,root,ans):
        if not root:
            return -1 
        
        left = self.getHeight(root.left,ans)
        right = self.getHeight(root.right,ans)
        
        curr = max(left,right) + 1
        ans[curr].append(root.val)
        return curr
    
        
        