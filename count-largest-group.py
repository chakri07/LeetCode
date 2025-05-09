"""
You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104


https://leetcode.com/problems/count-largest-group/
"""
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_num(n):
            s = 0 
            while n >=1 :
                digit = n % 10 
                s += digit 
                n = n // 10

            return s

        c_map = defaultdict(list)

        for num in range(1,n+1):
            c_map[sum_num(num)].append(num)

        max_len = 0 

        ans = 0 

        for _,arr_val in c_map.items():
            max_len = max(max_len, len(arr_val))

        for _,arr_val in c_map.items():
            if max_len == len(arr_val):
                ans += 1

        return ans
