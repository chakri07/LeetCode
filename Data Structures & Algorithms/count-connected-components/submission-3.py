from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        ans = 0

        adjMap = defaultdict(list)

        for start,end in edges:
            adjMap[start].append(end)
            adjMap[end].append(start)
        
        print(adjMap)


        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            children = adjMap[node]
            for child in children:
                dfs(child)


        for node in range(n):
            if node in visited:
                continue
            else:
                dfs(node)
                ans += 1

        return ans
