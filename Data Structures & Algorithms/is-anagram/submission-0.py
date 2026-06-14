class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}

        for char in s: 
            if char in map1: 
                map1[char] +=1 
            else: 
                map1[char] = 1
        
        map2 = {}
        for char in t: 
            if char in map2: 
                map2[char] +=1 
            else:
                map2[char] = 1
        
        return map1 == map2

        