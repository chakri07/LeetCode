"""

Course Schedule
Solved 
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.

https://neetcode.io/problems/course-schedule
"""

# DFS :
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = defaultdict(list)
        for p in prerequisites:
            prereq[p[1]].append(p[0])

        dp = {}

        #dfs and bfs rendu cheddam 
        def dfs(visited, course,dp):
            if course in dp:
                return dp[course]
            if course in visited:
                return False
            
            if len(prereq[course]) == 0:
                return True
            
            visited.add(course)
            for crs in prereq[course]:
                if not dfs(visited, crs):
                    dp[crs] = False
                    return False
                
            dp[course] = True
            return True
        
        for num in range(numCourses):
            visited = set()
            if not dfs(visited, num,dp):
                dp[num] = False
                return False
            dp[num] = True
        return True
    

## BFS solution 
# we add all the courses with no pre-reqs
# then figure out what all courses can we go from there
# when we are processing the child node we remove one from the number of pre-reqs
# as we are cmng from that pre_req and add it to the queue once number of pre-reqs
# are zero i.e) we have succesfully completed that particular courese

# we repear until queue == [] and check if finished count == numCourses count

from collections import defaultdict, deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degree = [0] * numCourses
        prereq = defaultdict(list)

        for a, b in prerequisites:
            in_degree[a] += 1
            prereq[b].append(a)


        # lets do BFS
        queue = deque()

        # append all the course with 0 pre reqs
        for num in range(numCourses):
            if in_degree[num] == 0:
                queue.append(num)

        fin = 0 
        
        while queue:
            crs = queue.popleft()
            fin += 1

            for nei in prereq[crs]:
                in_degree[nei] -=1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return fin == numCourses


 