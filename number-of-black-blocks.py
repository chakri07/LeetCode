"""

You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.

You are also given a 0-indexed 2D integer matrix coordinates, where coordinates[i] = [x, y] indicates that the cell with coordinates [x, y] is colored black. All cells in the grid that do not appear in coordinates are white.

A block is defined as a 2 x 2 submatrix of the grid. More formally, a block with cell [x, y] as its top-left corner where 0 <= x < m - 1 and 0 <= y < n - 1 contains the coordinates [x, y], [x + 1, y], [x, y + 1], and [x + 1, y + 1].

Return a 0-indexed integer array arr of size 5 such that arr[i] is the number of blocks that contains exactly i black cells.

 

Example 1:

Input: m = 3, n = 3, coordinates = [[0,0]]
Output: [3,1,0,0,0]
Explanation: The grid looks like this:

There is only 1 block with one black cell, and it is the block starting with cell [0,0].
The other 3 blocks start with cells [0,1], [1,0] and [1,1]. They all have zero black cells. 
Thus, we return [3,1,0,0,0]. 
Example 2:

Input: m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]
Output: [0,2,2,0,0]
Explanation: The grid looks like this:

There are 2 blocks with two black cells (the ones starting with cell coordinates [0,0] and [0,1]).
The other 2 blocks have starting cell coordinates of [1,0] and [1,1]. They both have 1 black cell.
Therefore, we return [0,2,2,0,0].


https://leetcode.com/problems/number-of-black-blocks"""

from typing import List

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        coods_set = set()
        for r, c in coordinates:
            coods_set.add((r, c))

        ans = [0] * 5

        candidate_top_left_corners = set()

        for r, c in coordinates:

            if r + 1 < m and c + 1 < n:
                candidate_top_left_corners.add((r, c))

            if r + 1 < m and c - 1 >= 0:
                candidate_top_left_corners.add((r, c - 1))

            if r - 1 >= 0 and c + 1 < n:
                candidate_top_left_corners.add((r - 1, c))

            if r - 1 >= 0 and c - 1 >= 0:
                candidate_top_left_corners.add((r - 1, c - 1))

        for r_tl, c_tl in candidate_top_left_corners:
            current_black_count = 0
            if (r_tl, c_tl) in coods_set:
                current_black_count += 1
            if (r_tl, c_tl + 1) in coods_set:
                current_black_count += 1
            if (r_tl + 1, c_tl) in coods_set:
                current_black_count += 1
            if (r_tl + 1, c_tl + 1) in coods_set:
                current_black_count += 1
            
            ans[current_black_count] += 1

        total_2x2_blocks = (m - 1) * (n - 1)
        
        counted_blocks_sum = sum(ans[1:]) 

        ans[0] = total_2x2_blocks - counted_blocks_sum

        return ans