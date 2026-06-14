from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words):
        """
        Determines the order of characters in a foreign dictionary based on sorted words.
        
        Args:
            words: List of strings sorted according to the foreign dictionary
            
        Returns:
            String representing the character order, or empty string if invalid
        """
        if not words:
            return ""
        
        # Build graph and indegree count
        graph = defaultdict(set)
        indegree = defaultdict(int)
        
        # Initialize all characters
        for word in words:
            for char in word:
                indegree[char] = 0
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            
            # Check for invalid case: longer word is prefix of shorter word
            if self._is_invalid_prefix(first, second):
                return ""
            
            # Find first differing character to establish ordering
            self._add_edge(first, second, graph, indegree)
        
        # Perform topological sort using Kahn's algorithm
        return self._topological_sort(graph, indegree)
    
    def _is_invalid_prefix(self, first, second):
        """Check if first word is longer and a prefix of second word (invalid case)"""
        min_len = min(len(first), len(second))
        return (len(first) > len(second) and 
                first[:min_len] == second[:min_len])
    
    def _add_edge(self, first, second, graph, indegree):
        """Add edge between first differing characters of two words"""
        min_len = min(len(first), len(second))
        
        for j in range(min_len):
            if first[j] != second[j]:
                # Only add edge if it doesn't already exist
                if second[j] not in graph[first[j]]:
                    graph[first[j]].add(second[j])
                    indegree[second[j]] += 1
                break  # Only care about first difference
    
    def _topological_sort(self, graph, indegree):
        """Perform topological sort to determine character ordering"""
        # Start with characters that have no incoming edges
        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            # Process all neighbors
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if topological sort is valid (no cycles)
        if len(result) != len(indegree):
            return ""  # Cycle detected
        
        return "".join(result)