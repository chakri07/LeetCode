'''
You are given two lists of closed intervals, firstlist and secondlist, where firstlist[i] = [starti, endi] and secondlist[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstlist = [[0,2],[5,10],[13,23],[24,25]], secondlist = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstlist = [[1,3],[5,9]], secondlist = []
Output: []
Example 3:

Input: firstlist = [], secondlist = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstlist = [[1,7]], secondlist = [[3,10]]
Output: [[3,7]]
'''


class Solution:
    def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
        pos1 = 0
        pos2 = 0
        ans = []
        while pos1 <len(firstlist) and pos2 < len(secondlist):
            intersection = self.helper(firstlist[pos1],secondlist[pos2])
            if intersection:
                ans.append(intersection)
                    
            if firstlist[pos1][1] < secondlist[pos2][1]:
                pos1 = pos1 + 1
            else :
                pos2 = pos2 + 1
                
        return ans
            
    
    def helper(self,set1: list[int],set2:list[int]) -> list[int]:
        low = 0
        high = 0 
        if set1[0] >= set2[0] and set1[0] <= set2[1]:
            low = set1[0]
            if set1[1] < set2[1]:
                high = set1[1]
            else:
                high = set2[1]
        elif  set2[0] >= set1[0] and set2[0] <= set1[1]:
            low = set2[0]
            if set1[1] < set2[1]:
                high = set1[1]
            else:
                high = set2[1]    
        else: 
            return
        ans = [low,high]
        return ans
            
        
        
        
        
            
            
        