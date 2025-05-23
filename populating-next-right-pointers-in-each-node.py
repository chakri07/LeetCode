"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



https://leetcode.com/problems/populating-next-right-pointers-in-each-node
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root):
        queue = deque([])
        child_queue = deque([])

        queue.append(root)

        if not root:
            return root

        while queue:
            node = queue.popleft()
            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)

            if queue:
                node.next = queue[0]
            else:
                queue = child_queue.copy()
                child_queue = deque([])
                node.next = None

        return root
        