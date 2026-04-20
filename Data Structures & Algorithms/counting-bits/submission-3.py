class Solution:
    # Solution: Cheating
    def countBits(self, n: int) -> List[int]:
        # Solution 1: cheating a bit Time/Space: O(n)
        # nums = []

        # for i in range(n+1):
        #     nums.append(len(bin(i)[2:].replace('0', '')))
        
        # return nums
    
        # Solution 2: Time/Space: O(nlogn)/O(n)
        # nums = []

        # for i in range(n+1):
        #     count = 0
        #     x = i

        #     while x:
        #         if x % 2:
        #             count += 1
        #         x = x >> 1
        #     nums.append(count)
        
        # return nums

        # Solution 3 - Time/Space: 0(n)
        dp = [0] * (n + 1)
        ans = [0]
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

        
        