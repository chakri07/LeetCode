"""

Number of Connected Components in an Undirected Graph
Solved 
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
https://neetcode.io/problems/count-connected-components
"""

# BFS
from collections import deque, defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS cheyali
        visited = set()
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


# DFS
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
