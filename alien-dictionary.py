"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

https://leetcode.com/problems/alien-dictionary
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Build the graph and initialize indegrees
        # Use a set for adjacency list values to avoid duplicate edges
        graph = defaultdict(set) 
        indegree = defaultdict(int)
        
        # Collect all unique characters and initialize their indegrees to 0
        all_chars = set()
        for word in words:
            for char in word:
                all_chars.add(char)
                indegree[char] = 0 # Explicitly set indegree to 0 for all chars

        # Step 2: Extract relationships (edges) from sorted words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            
            min_len = min(len(word1), len(word2))

            found_diff = False
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # Found the first differing character, establish order
                    if word2[j] not in graph[word1[j]]: # Prevent duplicate edges
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    found_diff = True
                    break
            
            # Case 3: Handle invalid ordering where word2 is a prefix of word1
            # e.g., ["abc", "ab"] -> invalid
            if not found_diff and len(word1) > len(word2):
                return "" # Invalid order (e.g., "abc" before "ab")

        # Step 3: Topological Sort (Kahn's Algorithm)
        queue = deque()
        # Add all characters with an indegree of 0 to the queue
        for char in all_chars: # Iterate through all known characters
            if indegree[char] == 0:
                queue.append(char)

        result_list = [] # Build result as a list of characters

        while queue:
            char = queue.popleft()
            result_list.append(char)

            # For each neighbor of the current character
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                # If neighbor's indegree becomes 0, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Cycle Detection
        # If the length of the result list is not equal to the total number of unique characters,
        # it means a cycle was detected.
        if len(result_list) != len(all_chars):
            return "" # Cycle detected, no valid order

        return "".join(result_list)
