from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def compare(big_hash,small_hash):
            for char in small_hash.keys():
                if big_hash[char] < small_hash[char]:
                    return False
            return True


        ans_start,ans_end = 0,float('inf')
        start,end = 0,0
        
        if len(s) < len(t):
            return ""
        
        t_hash = defaultdict(int)
        for char in t:
            t_hash[char]+= 1

        s_hash = defaultdict(int)
        while end < len(s):
            s_hash[s[end]] +=1
            while compare(s_hash,t_hash):
                if end - start < ans_end - ans_start:
                    ans_start,ans_end = start,end
                s_hash[s[start]] -= 1
                start += 1
            
            end += 1
        
        if ans_end == float('inf'):
            return ""
        return s[ans_start:ans_end+1]


