class Solution:
    def hammingWeight(self, n: int) -> int:
        # attempt 1
        # res = 0

        # while n:
        #     if n % 2 == 1:
        #         res += 1
        #     n = n >> 1
        
        # return res

        # attempt 2
        res = 0

        while n:
            n = n & (n-1)
            res += 1
        
        return res