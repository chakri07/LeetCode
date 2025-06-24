# import requests
# import mysql.connector
# import pandas as pd

"""
You have a bounded 2D grid with rows × cols blocks. Each block (r,c) can host multiple restaurants, each of which can be open or closed. Initially, every block has zero restaurants (i.e., no open restaurants anywhere).

You want to design a data structure with the following operations:
- openRestaurant(r, c)
    Adds a new open restaurant to block (r, c).
    If the block already had open restaurants, simply increments the count.
- countOpenRestaurants(r, c)
    Returns how many restaurants on block (r, c) are currently open.
    Returns 0 if there are no open restaurants at (r, c).
- hasOpenRestaurant(r, c)
    Returns true if there’s at least one open restaurant on (r, c), else false.
- countDeliveryZones()
    Returns the number of distinct delivery zones in the city.
    A “delivery zone” is defined as a maximal group of connected blocks (connected via up/down/left/right) that each have at least one open restaurant.
"""


print('Hello')
# optimize for countDeliveryZones


from collections import defaultdict


class UnionFind():
    # n = total num of cells
    def __init__(self):
        
        # (r, c)
        self.parent = {}
        # this might a dict
        self.size = defaultdict(lambda: 1)
        # self.size = [[1] * c]
        
        self.del_zone = 0
        
    def findParent(self, id):
        if id in self.parent:
            if self.parent[id] == id:
                return id
            else:
                parent = self.findParent(self.parent[id])
                self.parent[id] = parent
                return parent
                
        else:
            self.parent[id] = id
            return id
            
    def union(self, id1, id2):
        
        id1_parent = self.findParent(id1)
        
        id2_parent = self.findParent(id2)
 
        if id1_parent != id2_parent:
            if self.size[id1_parent] < self.size[id2_parent]:
                self.parent[id1_parent] = id2_parent
            elif self.size[id1_parent] > self.size[id2_parent]:
                self.parent[id2_parent] = id1_parent
            else:
                self.parent[id1_parent] = id2_parent
                self.size[id2_parent] += self.size[id1_parent]
            
            self.del_zone -= 1
            
            return True
        else:
            # print(self.del_zone)
            return False
        
"""
You want to design a data structure with the following operations:
- openRestaurant(r, c)
    Adds a new open restaurant to block (r, c).
    If the block already had open restaurants, simply increments the count.
- countOpenRestaurants(r, c)
    Returns how many restaurants on block (r, c) are currently open.
    Returns 0 if there are no open restaurants at (r, c).
- hasOpenRestaurant(r, c)
    Returns true if there’s at least one open restaurant on (r, c), else false.
- countDeliveryZones()
    Returns the number of distinct delivery zones in the city.
    A “delivery zone” is defined as a maximal group of connected blocks (connected via up/down/left/right) that each have at least one open restaurant.
"""


class Tracker:
    def __init__(self, rows, cols):
        
        self.grid = [[0] * cols for _ in range(rows)]
        self.uf = UnionFind()
        self.rows = rows
        self.cols = cols
    
    # validation can be a helper function
    def openRestaurant(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            if self.grid[r][c] == 0:
                # union find
                self.grid[r][c] += 1
                self.uf.del_zone += 1
                
                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                      
                for dr, dc in dirs:
                    nr, nc = r +dr, c+dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] > 0:
                        self.uf.union( (r,c), (nr,nc))    
            else:
                self.grid[r][c] += 1
                
                  
    def countOpenRestaurants(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        
        return -1
            
    def hasOpenRestaurant(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c] > 0
        
        return False
        
    def countDeliveryZones(self):
        return self.uf.del_zone
        
            


test_tracker = Tracker(3,4)

print(test_tracker.grid)

test_tracker.openRestaurant(0,0)
test_tracker.openRestaurant(2,0)


print(test_tracker.countDeliveryZones())

test_tracker.openRestaurant(1,0)

print(test_tracker.countDeliveryZones())


print(test_tracker.hasOpenRestaurant(0,0))
print(test_tracker.hasOpenRestaurant(2,3))

test_tracker.openRestaurant(0,0)

print(test_tracker.countOpenRestaurants(0,0))
print(test_tracker.countOpenRestaurants(2,3))

print(test_tracker.countOpenRestaurants(2,5))


print(test_tracker.hasOpenRestaurant(2,5))



test_tracker = Tracker(0,0)
print(test_tracker.openRestaurant(1,1))

s = Tracker(100, 100)

print(s.countOpenRestaurants(1,1)) # 0
s.openRestaurant(1,1)
s.openRestaurant(3,1)
s.openRestaurant(1,1)
print(s.countDeliveryZones()) # 2
s.openRestaurant(2,1)
print(s.countDeliveryZones()) # 1
s.openRestaurant(3,3)
s.openRestaurant(2,1)
print(s.countDeliveryZones()) # 2
s.openRestaurant(3,2)
print(s.countDeliveryZones()) # 1
print(s.countOpenRestaurants(2,2)) # 0
print(s.countOpenRestaurants(2,1)) # 2
print(s.countOpenRestaurants(42,71)) # 0
s.openRestaurant(17,12)
print(s.countDeliveryZones()) # 2
s.openRestaurant(17,14)
print(s.countDeliveryZones()) # 3
s.openRestaurant(16,13)
print(s.countDeliveryZones()) # 4
s.openRestaurant(16,12)
print(s.countDeliveryZones()) # 3
s.openRestaurant(18,13)
print(s.countDeliveryZones()) # 4
s.openRestaurant(17,13)
print(s.countDeliveryZones()) # 2