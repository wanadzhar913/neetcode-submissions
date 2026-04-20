class Solution:
    def hammingWeight(self, n: int) -> int:
        # attempt 1
        from collections import Counter

        return Counter(bin(n))['1']
        