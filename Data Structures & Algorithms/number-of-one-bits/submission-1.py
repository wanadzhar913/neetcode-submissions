class Solution:
    def hammingWeight(self, n: int) -> int:
        # attempt 1 (sus!)
        from collections import Counter

        return Counter(bin(n))['1']

        # attempt 2
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
        