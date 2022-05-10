'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Link:https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ref = {'2': "abc"
                , '3': "def"
                , '4': "ghi"
                , '5': "jkl"
                , '6': "mno"
                , '7': "pqrs"
                , '8': "tuv"
                , '9': "wxyz"}
        output = []
        
        for digit in digits:
            digit_str = ref[digit]
            output = self.helper(digit_str,output)
        return output
            
    def helper(self,digit_str:str,output:list[list[int]]):
        ans = []
       
        if len(output) ==0 :
            for letter in digit_str:
                output.append(letter)
            return output
        else:
            for letter in digit_str:
                for word in output:
                    new_word = word + letter
                    ans.append(new_word)
        return ans