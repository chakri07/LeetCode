# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        level = []
        child_queue = []

        while queue:
            node = queue[0]
            level.append(node.val)
            queue.remove(node)
            if node.left:
                child_queue.append(node.left) 
            if node.right:
                child_queue.append(node.right) 
            if len(queue) == 0:
                queue = child_queue
                child_queue = []
                ans.append(level)
                level = []

        return ans
                
