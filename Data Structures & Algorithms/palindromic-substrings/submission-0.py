class Solution:
    def countSubstrings(self, s: str) -> int:
         
        def helper(left,right):
            ans = 0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans +=1
                print(ans)
                left -=1 
                right +=1
            return ans
        
        
        final = 0 

        for i in range(len(s)):
            one_count = helper(i,i)
            two_count = helper(i,i+1)
            final += one_count
            final += two_count 
        
        return final
        



        