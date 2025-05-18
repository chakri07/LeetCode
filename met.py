QUESTION 2 
You’ve been tasked to help a village find the best place to install a new well. You’re given a 2D grid where cells can be empty, a house, or a tree. People can walk up, down, left and right, but they can’t walk through trees. Place the well that minimizes the total sum distance from all the houses.


- - - - -
- H T - -
- - T H -
- T H - -
- - - - -


from collections import deque
def helper(grid):
    neighs = [(-1,0),(1,0),(0,1),(0,-1)]
    
    rows = len(grid)
    cols = len(grid[0])

    dp = {}

    def find_distance(sr,sc,er,ec,visited):
        if (sr,sc,er,ec) in dp:
            return dp[(sr,sc,er,ec)] 

        queue = deque([(sr,sc,0)])
        visited.add((sr,sc))

        while queue:
            r,c,curr_dist = queue.popleft()
            
            curr_dist +=1

            for dr,dc in neighs:
                nr,nc = r+dr, c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != 'T' and (nr,nc) in visited:
                        if (nr,nc) == (er,ec):
                            dp[(sr,sc,er,ec)] = curr_dist
                            return dp[(sr,sc,er,ec)]

                        visited(nr,nc)
                        queue.append((nr,nc,curr_dist))
    
    # actual logic
    ans_dist = float('inf')
    ans = []
    house_coords = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'H':
                house_coords.append((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'T' or grid[r][c] != 'H':
                # final loop tp find dista
                curr_distnace = 0 
                for hr,hc in house_coords:
                    visited = set()
                    curr_distnace += find_distance(hr,hc, r, c, visited)

                if curr_distance < ans_dist:
                    ans_dist = curr_distance
                    ans = [r,c]

    return ans
