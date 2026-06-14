class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []

        intervals.sort()
        
        ans.append(intervals[0])
        
        for inter in intervals[1:]:
            if inter[0] > ans[-1][1]:
                ans.append(inter)
                continue
            else:
                if inter[1] > ans[-1][1]:
                    ans[-1][1] = inter[1]
                    
        return ans