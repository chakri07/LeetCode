"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs use cheyali 

        def dfs(node,visited):
            if not node:
                return None
            
            if node in visited:
                return visited[node]

            
            ans = Node()
            ans.val = node.val

            visited[node] = ans
            
            for n in node.neighbors:
                ans.neighbors.append(dfs(n,visited))

            print(ans.val)
            print(ans.neighbors)
            return ans
        
        visited = {}
        return dfs(node,visited)