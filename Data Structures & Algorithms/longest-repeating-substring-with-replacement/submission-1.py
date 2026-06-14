import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        import heapq

        ans = 0
        max_freq = float('-inf')
        count = collections.defaultdict(int)
        left = 0

        for right in range(len(s)):
            count[s[right]] +=1
            max_freq = max(max_freq,count[s[right]])

            while (right -left - max_freq +1) > k:
                count[s[left]] -=1
                left = left + 1

            ans = max(ans,right-left +1)

        return ans

