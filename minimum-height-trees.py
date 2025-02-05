"""
310. Minimum Height Trees
Attempted
Medium
Topics
Companies
Hint
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

https://leetcode.com/problems/minimum-height-trees/description/
"""

# Key Insight:
# The MHTs are the centroids of the tree. In a tree, the centroids are the nodes that are "in the middle" of the longest paths. There can be either 1 or 2 centroids in a tree.

# Intuition:
# Leaves: Nodes with only one connection (degree = 1) are called leaves.

# Removing Leaves: If we repeatedly remove leaves from the tree, we will eventually be left with the centroids.

# Why This Works: The centroids are the last nodes remaining because they are the most "central" nodes in the tree. Removing leaves layer by layer is like peeling an onion until we reach the core.

# Using centroid logic
from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adjlist = defaultdict(list)
        degree =[0] * n
        for src,dest in edges:
            adjlist[src].append(dest)
            adjlist[dest].append(src)
            degree[src] +=1
            degree[dest] +=1

        queue = deque([])
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        remaining = n

        while remaining > 2:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                degree[node] -= 1
                remaining -= 1
                childs = adjlist[node]
                for child in childs:
                    degree[child] -= 1
                    if degree[child] == 1:
                        queue.append(child)
                
        return list(queue)

# Brute force exceeds time limit
# find distance of each node from each other.
from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        adjlist = defaultdict(list)
        for src,dest in edges:
            adjlist[src].append(dest)
            adjlist[dest].append(src) 

        # populating the diagonal
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 0
        
        for i in range(n):
            visited = set()
            visited.add(i)

            queue = deque(adjlist[i])
            child_queue = deque([])
            curr_dist = 1
            while queue:
                node = queue.popleft()
                visited.add(node)
                dp[i][node] = min(dp[i][node],curr_dist)
                for child in adjlist[node]:
                    if child not in visited:
                        child_queue.append(child)

                if len(queue) == 0:
                    queue = child_queue
                    child_queue = deque([])
                    curr_dist +=1
        
        # we need min of max Distances
        ans = float('inf')

        max_arr = []
        for i in range(n):
            max_val = float('-inf')
            for j in range(n):
                max_val = max(max_val,dp[i][j])

            max_arr.append(max_val)
            ans = min(ans,max_val)
        
        ans_arr = []
        for i in range(n):
            if max_arr[i] == ans:
                ans_arr.append(i)
        
        return ans_arr
