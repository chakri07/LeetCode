class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(32):
            digit = n & 1
            res = res + (digit << (31 - i))

            n = n >> 1

        return res
        