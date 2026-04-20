class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution #1 Trivial: Time: O(n), Space: O(1)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # Solution #2
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # left sorted portion of the array
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            # right sorted portion of the array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: # target > nums[m] and target < nums[r]
                    l = m + 1

        return -1

            

