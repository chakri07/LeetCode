"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary
"""

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        # pre compute values 
        cnt_map = defaultdict(int)

        mod = 10 **9 + 7

        for word in words:
            for i, char in enumerate(word):
                cnt_map[(i,char)] += 1
        

        dp = defaultdict(int) 

        def helper(target_idx, word_idx):
            if target_idx >= len(target):
                # we reached the edn 
                return 1 
            
            if word_idx >= len(words[0]):
                return 0
            
            if (target_idx, word_idx) in dp:
                return dp[(target_idx, word_idx)]

            """
            2 choices 
            1.pick one of the lettres
            2. Dont pick even if matches
            """

            count_dont_pick = helper(target_idx, word_idx+1)

            char = target[target_idx]
            count_pick = 0
            if cnt_map[(word_idx,char)] > 0:
                count_pick = helper(target_idx + 1, word_idx+1) * cnt_map[(word_idx,char)]

            dp[(target_idx, word_idx)] = (count_dont_pick + count_pick) % mod

            return dp[(target_idx, word_idx)]

        return helper(0,0) % mod
