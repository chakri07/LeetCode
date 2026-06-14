class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 0 : 
            return True

        for char in s:
            if char in [')', '}',']'] and len(stack) == 0 : 
                return False
            if char in ['(', '{', '['] :
                stack.append(char)
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            else:
                stack.pop(-1)




        return len(stack) == 0 
            
            

        