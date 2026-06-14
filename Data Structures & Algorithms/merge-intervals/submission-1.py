class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 : 
            return []

        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        print(sorted_intervals)

        ans = [sorted_intervals[0]]

        for interval in sorted_intervals[1:]:
            start = interval[0]
            end = interval[1]

            prev_start = ans[-1][0]
            prev_end = ans[-1][1]
            
            if(start <= prev_end):
                ans[-1][1] = max(end,prev_end) 
            else :
                ans.append(interval)
        
        return ans

