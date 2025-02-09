"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

https://leetcode.com/problems/top-k-frequent-words/description/
"""

# what is o(nlog(k)) and O(n) solution .?
# we maintain a heap of size k 
# remove the least frequent until that point 
# if we have to
from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # Step 1: Build frequency map
        freq_map = Counter(words)  # O(N) time

        # Step 2: Use a min-heap of size K
        min_heap = []
        
        for word, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, word))
            if len(min_heap) > k:  # Maintain heap of size K
                heapq.heappop(min_heap)

        # Step 3: Extract elements in sorted order
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])  # Extract words
        
        return result[::-1]  # Reverse to get highest frequency first



# o(nlog(n)) and O(n) solution

from collections import defaultdict
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq_map = defaultdict(int)

        for word in words:
            freq_map[word] +=1

        max_heap = []
        heapq.heapify(max_heap)

        for key,val in freq_map.items():
            heapq.heappush(max_heap,( -1 * val, key))

        ans = []
        for i in range(k):
            freq, word = heapq.heappop(max_heap)
            ans.append(word)
        
        return ans
