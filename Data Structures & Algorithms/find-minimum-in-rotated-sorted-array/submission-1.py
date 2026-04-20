class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution: Time: O(n), Space: O(1)
        # min_num = nums[0]
        # for i in nums:
        #     min_num = min(min_num, i)
        
        # return min_num

        # Solution
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # results are already sorted here
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res