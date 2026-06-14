class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #  we are assuming the solution is unique 
        t_map = {}

        for char in t:
            if char in t_map:
                t_map[char] += 1 
            else:
                t_map[char] = 1
            
        ans = [0,0,float('inf')]
        
        left = 0 
        right = 0
        s_map = {}

        required = len(t_map)
        formed = 0 

        while left <= right and right < len(s):
            char = s[right]
            if char in t_map:
                if char in s_map:
                    s_map[char] += 1
                else:
                    s_map[char] = 1 
                
                if t_map[char] == s_map[char]:
                    formed += 1 

                while formed == required:
                    if ans[2] > (right - left + 1):
                        ans = [left, right, right - left + 1]
                    
                    l_char = s[left]
                    if l_char in t_map:
                        s_map[l_char] -= 1
                        if t_map[l_char] > s_map[l_char]:
                            formed -=1 
                        if s_map[l_char] == 0:
                            del s_map[l_char]

                    left +=1 

            right += 1

        if ans[2] == float('inf'):
            return ''
        
        return s[ans[0]:ans[1]+1]
            


