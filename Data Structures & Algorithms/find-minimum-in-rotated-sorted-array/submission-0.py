class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution
        min_num = nums[0]
        for i in nums:
            min_num = min(min_num, i)
        
        return min_num


        # Solution 
        # l, r = 0, len(nums) - 1


