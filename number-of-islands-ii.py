"""
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.




https://leetcode.com/problems/number-of-islands-ii
"""

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
        self.rank = [1] * n 

        self.num_sets = 0 

    def find_par(self, i):
        if self.parent[i] == i:
            return i 
        
        self.parent[i] = self.find_par(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        # union only possible if parents are not same
        # else not needed
        i_par = self.find_par(i)
        j_par = self.find_par(j) 
        if i_par != j_par:
            if self.rank[i_par] < self.rank[j_par]:
                #change the parent 
                self.parent[i_par] = j_par
            elif self.rank[i_par] > self.rank[j_par]:
                self.parent[j_par] = i_par
            else:
                self.parent[i_par] = j_par
                self.rank[j_par] += 1

            self.num_sets -= 1
            return True
        
        return False

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Initialize Union-find_par for m*n cells
        # We use a 1D array to represent the 2D grid
        uf = UnionFind(m * n)

        visited = [[False] * n for _ in range(m)]

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        ans = []
        for r,c in positions:
            if visited[r][c]:
                ans.append(uf.num_sets)
                continue
            
            visited[r][c] = True

            uf.num_sets += 1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc 
                if 0 <= nr < m and 0 <= nc < n:
                    if visited[nr][nc]:
                        curr_node_id = r * n + c 
                        new_node_id = nr * n + nc
                        uf.union(curr_node_id, new_node_id)

            ans.append(uf.num_sets)

        return ans

            














        