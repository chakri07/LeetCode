from collections import deque, defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS cheyali
        visited = set()
        queue = deque([0])

        adjMap = defaultdict(set)

        for start,end in edges: 
            adjMap[start].add(end)
            adjMap[end].add(start)

        def bfs(node):
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                if not curr in visited:
                    visited.add(curr)
                    queue.extend(adjMap[curr] - visited) 
        
        ans = 0

        for node in range(n):
            if not node in visited:
                bfs(node)
                ans += 1 
            
        return ans