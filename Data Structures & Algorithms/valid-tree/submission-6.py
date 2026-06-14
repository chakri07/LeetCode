from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        visited = set()
        adjList = defaultdict(list)
    
        for srt,end in edges:
            adjList[srt].append(end)
            adjList[end].append(srt)

        def dfs(root,parent):
            if root in visited: # cycle detection
                return False
            visited.add(root)
            for nei in adjList[root]:
                if nei == parent:
                    continue
                if not dfs(nei,root):
                    return False

            return True

        return dfs(0,-1) and len(visited) == n



            



        

            