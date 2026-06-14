class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counts = collections.defaultdict(int)
        l = 0
        max_val = float('-inf')
        
        for r in range(0,len(s)):
            counts[s[r]]+=1
            if counts[s[r]] > max_val:
                max_val = max(counts.values())
            while r-l + 1 - (max_val) > k:
                counts[s[l]]-=1
                l = l + 1
            ans = max(ans,r-l+1)
            
        return ans