class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals,key = lambda x:x[0])
        print(intervals)

        # we have ecerything in sorted order 
        ans = [intervals[0]]
        for start,end in intervals[1:]:
            if start > ans[-1][1]:
                ans.append([start,end])
            else:
                ans[-1][1] = max(end,ans[-1][1])
        
        return ans
