from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        for num in nums:
            next_sums = defaultdict(int)
            for s,freq in sums.items():
                next_sums[s+num] = next_sums[s+num] + sums[s]
                next_sums[s-num] = next_sums[s-num] + sums[s]

            sums = next_sums

        return next_sums[target]

