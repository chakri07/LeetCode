from collections import deque, defaultdict
import heapq 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1 
        
        heap = []
        for task, freq in freq_map.items():
            heapq.heappush(heap,(-freq,task))

        queue = deque()
        cycles = 0 

        while heap or queue:
            while queue and queue[0][0] <= cycles:
                _, freq, task = queue.popleft()
                if freq < 0:
                    heapq.heappush(heap, (freq, task))

            if heap:
                freq, task = heapq.heappop(heap)
                if freq + 1 < 0:
                    queue.append((cycles + n + 1, freq + 1, task))

            cycles += 1

        return cycles