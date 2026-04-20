class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution #1: Time - O(n^2), Space - O(1)
        # Reasoning: Your loop runs `n` times (the range is `len(nums) + 1`).
        # Inside that loop, the line `if i not in nums` performs a linear
        # search on the list. A search inside a loop means you are essentially
        # doing `n * n` work.
        # x = 0

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         x += i
        
        # return x

        # Solution #2
        return abs(sum(nums) - sum(range(len(nums) + 1)))



        