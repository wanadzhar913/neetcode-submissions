class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False




















        # brute force
        # seen = []
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.append(i)
        # return False

        nums.sort()
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        return False # Time: O(nlogn), Space: O(1)

        # solution
        # hashset = set()
        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        # return False # Time O(n), Space O(n)



        