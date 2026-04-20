class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution #1 Brute Force
        # output = []

        # for i in range(len(nums)):
        #     x = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             x *= nums[j]
        #     output.append(x)

        # return output

        # Solution #2
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



