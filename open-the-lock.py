'''

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

https://leetcode.com/problems/open-the-lock/
'''
from collections import defaultdict
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        visited = set(deadends)
        start = '0000'

        # each position can ge forward or backward
        queue = deque([start])

        if '0000' in visited:
            return -1
        
        visited.add('0000')

        moves = 0 

        while queue:
            curr_level = len(queue)
            for i in range(curr_level):
                curr = queue.popleft()
                if curr == target:
                    return moves
                
                for i in range(4):
                    digit = int(curr[i])
                    for move in [-1, 1]:
                        new_digit = (digit + move) % 10
                        new_combo = curr[:i] + str(new_digit) + curr[i+1:]
                        if new_combo not in visited:
                            visited.add(new_combo)
                            queue.append(new_combo)

            moves += 1

        return -1
    

import collections
class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
