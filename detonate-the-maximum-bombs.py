"""

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.


https://leetcode.com/problems/detonate-the-maximum-bombs
"""

from collections import defaultdict
from typing import List
from collections import defaultdict, deque

# Bfs solution
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # a point is in cirle if 

                b1x, b1y, b1r = bombs[i]
                b2x, b2y, b2r = bombs[j]
                if (b1x- b2x) ** 2 + (b1y - b2y)** 2 <= b1r**2:
                    # means inside
                    graph[i].append(j)


        def bfs(i):

            visited = set()
            queue = deque([i])
            ans = 0
            visited.add(i)
            

            while queue:
                curr_bomb = queue.popleft()
                ans += 1

                for neigh in graph[curr_bomb]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

            return ans

        final_ans = 0
        for i in range(n):
            final_ans = max(final_ans, bfs(i))

        
        return final_ans


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        # Build graph: bomb i can detonate bomb j if j is in range of i
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist_sq <= r1 ** 2:
                    graph[i].append(j)

        # DFS to count total detonations from a starting bomb
        def dfs(start, visited):
            visited.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    dfs(nei, visited)
        
        max_detonated = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            max_detonated = max(max_detonated, len(visited))

        return max_detonated
