class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start = start + 1
            while start < end and not s[end].isalnum():
                end = end - 1
            if s[end].lower() != s[start].lower():
                return False
            else :
                start = start + 1
                end = end - 1
        return True