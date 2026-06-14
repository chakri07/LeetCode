from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = defaultdict(list)
        for p in prerequisites:
            prereq[p[1]].append(p[0])

        #dfs and bfs rendu cheddam 
        def dfs(visited, course):
            if course in visited:
                return False
            
            if len(prereq[course]) == 0:
                return True
            
            visited.add(course)
            for crs in prereq[course]:
                if not dfs(visited, crs):
                    return False
            
            return True
        

        
        for num in range(numCourses):
            visited = set()
            if not dfs(visited, num):
                return False
        return True