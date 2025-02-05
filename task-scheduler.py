'''

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].


https://leetcode.com/problems/task-scheduler/
'''

# we have to use queue plus max heap 

# queue for the time remaning - initially zero size
# max heap with most frequent tasks.
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        import heapq
from collections import Counter, deque

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = Counter(tasks)  # Count frequency of each task
        max_heap = [-count for count in task_counts.values()]  # Max heap (invert sign)
        heapq.heapify(max_heap)  # Convert list into a heap
        
        queue = deque()  # Stores (time_available, frequency) of tasks in cooldown
        time = 0  # Keeps track of time units
        
        while max_heap or queue:
            time += 1
            
            # Process available task (if any)
            if max_heap:
                freq = heapq.heappop(max_heap) + 1  # Pop most frequent task (-ve sign)
                if freq < 0:  # If tasks are remaining, push to cooldown queue
                    queue.append((time + n, freq))
            
            # Check if any task in cooldown is ready to be executed again
            if queue and queue[0][0] == time:
                heapq.heappush(max_heap, queue.popleft()[1])  # Re-add task to heap
        
        return time


import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = collections.defaultdict(int)
        for s in tasks:
            freq_map[s] +=1 
            
        freqs = list(freq_map.values())
        freqs.sort()
        f_max = freqs.pop()
        
        idle_time = (f_max -1) * n
        
        while freqs and idle_time > 0:
            idle_time -= min(f_max-1,freqs.pop())
        
        idle_time = max(0,idle_time)
        
        return idle_time + len(tasks)