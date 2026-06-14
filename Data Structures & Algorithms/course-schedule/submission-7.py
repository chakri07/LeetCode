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
                if not dfs(visited, crs,dp):
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