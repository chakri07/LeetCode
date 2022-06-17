'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

# sorting approach
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans_map = {}
        for s in strs:
            temp = sorted(s)
            temp = str(temp)
            if temp in ans_map:
                ans_map[temp].append(s)   
            else:
                ans_map[temp] =[s]
                
        return ans_map.values()
                  
                  
# solve by counting elements
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_map = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)- ord('a')] += 1
                
            ans_map[tuple(count)].append(s)
            
        return ans_map.values()