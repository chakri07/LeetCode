'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Level order traversal solution
# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([])

        if not root:
            return []
        
        queue.append(root)
        child_queue = deque([])
        level = []
        ans = []
        right_side = []
        while queue:
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)
            
            if not queue:
                right_side.append(node.val)
                queue = child_queue
                child_queue = deque([])

                ans.append(level)
                level = []

        
        return right_side

        
 
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)

        # bfs
        child_queue = deque()
        level = []
        temp = []
        while queue:
            node  = queue.popleft()
            temp.append(node.val)
            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)
            
            
            if len(queue) == 0:
                queue = child_queue
                level.append(temp[:])
                child_queue = deque()
                temp = []
        
        ans = []

        for lev in level:
            ans.append(lev[-1])

        return ans


# Definition for a binary tree node.
from typing import Optional

# DFS
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []
        
        right = []
        def helper(root,level):
            if level == len(right):
                right.append(root.val)
            if root.right:
                helper(root.right,level+1)
            if root.left:
                helper(root.left,level+1)
            
        helper(root,0)
        return right

