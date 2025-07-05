"""

You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

Allocate a block of size consecutive free memory units and assign it the id mID.
Free all memory units with the given id mID.
Note that:

Multiple blocks can be allocated to the same mID.
You should free all the memory units with mID, even if they were allocated in different blocks.
Implement the Allocator class:

Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
int freeMemory(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
 

Example 1:

Input
["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Output
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

Explanation
Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
loc.freeMemory(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
loc.freeMemory(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
loc.freeMemory(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.
 

Constraints:

1 <= n, size, mID <= 1000
At most 1000 calls will be made to allocate and freeMemory.

https://leetcode.com/problems/design-memory-allocator
"""


class Allocator:

    def __init__(self, n: int):
        self.blocks = [] # it will store ranges ( start, end)
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        new_block = [0,size]
        if size <= 0 or size > self.n: # Added size <= 0 check
            return -1

        if not self.blocks:
            # start, end, mID
            self.blocks = [[0,size, mID]]
            return 0

        # lets see if we can see if block can sit in front
        
        if size <= self.blocks[0][0]:
            self.blocks = [[0,size, mID]] + self.blocks
            return 0 

        for i in range(1, len(self.blocks)):
            prev_start, prev_end, _ = self.blocks[i-1]
            next_start, next_end, _ = self.blocks[i]
            curr_start, curr_end = prev_end, prev_end+size

            # mean we can insert the block in between
            if curr_end <= next_start:
                self.blocks = self.blocks[:i] + [[curr_start, curr_end, mID]] + self.blocks[i:]
                return prev_end
            # else just go to the next block state
        
        # see if the block will go at the end 
        curr_start , curr_end = self.blocks[-1][1] , self.blocks[-1][1] + size
        if curr_end <= self.n:
            self.blocks +=  [[curr_start, curr_end, mID]]
            return curr_start
        
        return -1


    def freeMemory(self, mID: int) -> int:
        new_memory = []
        ans = 0
        for i in range(len(self.blocks)):
            _, _, mid = self.blocks[i]
            if mid != mID:
                new_memory.append(self.blocks[i])
            else:
                ans += (self.blocks[i][1] - self.blocks[i][0])

        self.blocks = new_memory
        return ans



from collections import defaultdict
class Allocator:

    def __init__(self, n: int):
        self.freeBlocks = SortedList([(0, n-1)]) # type: ignore
        self.busyBlocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for start, end in self.freeBlocks:
            if (blockEnd:=start+size-1) > end: continue # block size is not enough
            self.busyBlocks[mID].append((start, blockEnd))
            self.freeBlocks.remove((start, end))
            if blockEnd < end: # have free size in the block, return new free size to freeBlocks list
                self.freeBlocks.add((blockEnd+1, end))
            return start

        return -1 # no avaialbe blocks
        

    def freeMemory(self, mID: int) -> int:
        freeBlocksCnt = 0
        for start, end in self.busyBlocks[mID]:
            freeBlocksCnt += end - start + 1
            idx = self.freeBlocks.bisect_left((start, end))
            
            # first process block from the right, because after removing from the left
            # all blockes moved to the -1 position in self.freeBlocks
            if idx < len(self.freeBlocks): # check next free block if it does exist
                nextStart, nextEnd = self.freeBlocks[idx]
                if end + 1 == nextStart:
                    end = nextEnd
                    self.freeBlocks.remove((nextStart, nextEnd))

            # check left (previous) free block if it does exist
            if idx > 0: 
                prevStart, prevEnd = self.freeBlocks[idx - 1]
                if prevEnd + 1 == start:
                    start = prevStart
                    self.freeBlocks.remove((prevStart, prevEnd))

            self.freeBlocks.add((start, end))
        del self.busyBlocks[mID] # remove all released blocks
        
        return freeBlocksCnt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)