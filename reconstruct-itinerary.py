'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

https://leetcode.com/problems/reconstruct-itinerary/
'''

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        ite_map = {}
        
        for t in tickets:
            start = t[0]
            end = t[1]
            if start in ite_map.keys():
                ite_map[start].append(end)
            else:
                ite_map[start] = [end]
                
        for val in ite_map.values():
            val.sort()
        res = ['JFK']
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in ite_map:
                return False
            
            temp = list(ite_map[cur])
            for v in temp:
                ite_map[cur].pop(0)
                res.append(v)
                if dfs(v):
                    return res
                res.pop()
                ite_map[cur].append(v)
            return False     
        dfs("JFK")
        return res
            
            