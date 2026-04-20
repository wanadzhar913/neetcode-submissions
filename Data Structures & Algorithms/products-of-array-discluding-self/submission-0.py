class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution #1 Brute Force
        output = []

        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if j != i:
                    x *= nums[j]
            output.append(x)

        return output
