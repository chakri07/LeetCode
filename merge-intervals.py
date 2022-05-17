'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



https://leetcode.com/problems/merge-intervals/
'''

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
        
        