from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0

        chars = defaultdict(int)
        start = 0 
        end = 1 
        ans = 1
        chars[s[0]] = 1

        while end < len(s):
            curr_char = s[end]
            if curr_char in chars and chars[curr_char] > 0:
                ans = max(end-start, ans)

                chars[s[start]] -=1
                start = start + 1
            else:
                chars[s[end]] +=1 
                end = end + 1
                

        return max(ans,end-start)


            