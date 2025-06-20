"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

https://leetcode.com/problems/word-ladder
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0 

        l = len(beginWord)


        all_combos = defaultdict(list)

        for word in wordList:
            for i in range(l):
                all_combos[word[:i]+ '*' + word[i+1:]].append(word)


        queue = deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            curr_word, level = queue.popleft()
            for i in range(l):
                inter_word = (curr_word[:i]+ '*'+ curr_word[i+1:])

                for word in all_combos[inter_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited: 
                        visited.add(word)
                        queue.append((word, level+1))
        
        return 0
