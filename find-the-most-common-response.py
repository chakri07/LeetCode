"""

You are given a 2D string array responses where each responses[i] is an array of strings representing survey responses from the ith day.

Return the most common response across all days after removing duplicate responses within each responses[i]. If there is a tie, return the lexicographically smallest response.

 

Example 1:

Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

Output: "good"

Explanation:

After removing duplicates within each list, responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]].
"good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times.
Return "good" because it has the highest frequency.
Example 2:

Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]

Output: "bad"

Explanation:

After removing duplicates within each list we have responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]].
"bad", "good", and "ok" each occur 2 times.
The output is "bad" because it is the lexicographically smallest amongst the words with the highest frequency.


https://leetcode.com/problems/find-the-most-common-response
"""

from collections import defaultdict
from typing import List
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        r_map = defaultdict(int)
        for response in responses:
            response = set(response)

            for resp in response:
                r_map[resp] +=1 

        max_count = max(r_map.values())

        temp = []

        for resp,count in r_map.items():
            if count == max_count:
                temp.append(resp)

        return min(temp)