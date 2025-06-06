"""

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

https://leetcode.com/problems/graph-valid-tree
"""


from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        if n == 1: return True

        
        m = defaultdict(list)

        for a,b in edges:
            m[a].append(b)
            m[b].append(a)
        self.ans = True
        seen = set()
        def dfs(cur, parent):
            if self.ans == False:
                return 
            for nxt in m[cur]:
                if nxt in seen and nxt != parent:
                    self.ans = False
                    return 
                if nxt not in seen:
                    seen.add(nxt)
                    dfs(nxt, cur)
        seen.add(edges[0][0])
        dfs(edges[0][0], None)
        return self.ans if len(seen) == len(m) else False