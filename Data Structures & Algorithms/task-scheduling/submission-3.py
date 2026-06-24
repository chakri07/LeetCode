import heapq 
from collections import defaultdict, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        
        # we want max freq heap first
        heap = []
        for task, freq in freq_map.items():
            heapq.heappush(heap,(-freq, task))

        # time, freq, task
        queue = deque()
        time = 0

        while heap or queue:
            # check if any can be added back 
            while queue and time >= queue[0][0]:
                _, freq, task = queue.popleft()
                if freq < 0:
                    heapq.heappush(heap,(freq,task))

            if heap:
                freq,task = heapq.heappop(heap)
                if freq + 1 < 0:
                    queue.append((time+n+1, freq+1, task))
            
            time += 1 

        return time 



