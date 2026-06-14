from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. Convert wordList to a set for O(1) lookups
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        # 2. Initialize BFS queue: (current_word, current_path_length)
        # Start level is 1 because the problem counts the number of words in the sequence
        queue = deque([(beginWord, 1)])
        
        # 3. Track visited words to prevent infinite loops
        visited = set([beginWord])
        
        word_len = len(beginWord)
        
        # 4. Begin BFS
        while queue:
            curr_word, level = queue.popleft()
            
            # If we reached the target word, return the level immediately
            if curr_word == endWord:
                return level
            
            # Generate all possible 1-letter transformations (Implicit Graph)
            for i in range(word_len):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == curr_word[i]:
                        continue
                        
                    # Create the new mutated word
                    next_word = curr_word[:i] + c + curr_word[i+1:]
                    
                    # If it's a valid word and we haven't visited it yet
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                        
        return 0