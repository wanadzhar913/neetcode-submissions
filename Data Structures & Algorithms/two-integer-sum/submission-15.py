class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution (Brute Force): Space - O(n^2), Time - O(1)
        # initialize 2 pointers, i & j
        # i = 0
        # j = i + 1
        # for i in len(nums):
        # for j in range(i + 1, len(nums))
        # check if nums[i] + nums[j] == target
        # if yes, return [i, j]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Solution (Optimal)
        # initialize a seen hashmap. This will store:
        # item in nums (key), as well as position in array (value)
        # we'll iterate through enumerate(nums).
        # at each step, we'll:
        # a) check that the diff between target, needed, and current iteration, n, is in
        # seen
        # b) if yes, return seen[needed], i
        # else: seen[nums] = i
        # c) edge cases: what if duplicates e.g., [5, 5]? Shouldn't matter because
        
        seen = {}
        
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen.keys():
                return [seen[needed], i]
            else:
                # if duplicate, this gets updated with the later index
                seen[num] = i



        












        
        # Brute Force - Ugly
        # for i, n in enumerate(nums):
        #     if i < len(nums):
        #         for j, n in enumerate(nums[i+1:]):
        #             if nums[i] + nums[j+(i+1)] == target:
        #                 return [i, j+(i+1)]

        # Brute Force - But way cleaner
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimal
        # seen = {}
        # for i, num in enumerate(nums):
        #     needed = target - num
        #     if needed in seen:
        #         return [seen[needed], i]
        #     seen[num] = i

        # Solution 4 (if they are sorted)
        # n = len(nums)
        # l, r = 0, n - 1

        # while l<r:
        #     if nums[l] + nums[r] == target:
        #         return [l, r]
        #     elif nums[l] + nums[r] < target:
        #         l += 1
        #     elif nums[l] + nums[r] > target:
        #         r -= 1


