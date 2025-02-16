'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
'''

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # bfs we can do 
        # once we read from right the correct direction 
        # the other time we read from then opposite direction
        if not root:
            return []

        queue = deque([root])

        ans = []

        isReversed = False

        while queue:
            level = len(queue)
            curr_level = []

            for i in range(level):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if isReversed:
                curr_level = list(reversed(curr_level))
            
            ans.append(curr_level)
            isReversed = not isReversed

        return ans




import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = collections.defaultdict(list)
        self.helper(root,0,ans)
        return list(ans.values())

    def helper(self,root,level,ans):
        if not root:
            return
        if level in ans:
            if level %2 == 0:
                ans[level].append(root.val)
            else:
                ans[level].insert(0,root.val)
        else:
            ans[level] = [root.val]

        self.helper(root.left,level+1,ans)
        self.helper(root.right,level+1,ans)

