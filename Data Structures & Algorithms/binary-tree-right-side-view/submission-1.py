# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        child_queue = deque()
        queue.append(root)
        result = []

        while queue:
            node = queue.popleft()
            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)

            if not queue:
                result.append(node.val)
                queue = child_queue
                child_queue = deque()


        return result


        