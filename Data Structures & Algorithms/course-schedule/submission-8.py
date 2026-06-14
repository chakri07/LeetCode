from collections import defaultdict, deque

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


