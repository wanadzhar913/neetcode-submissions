class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a hashset
        # go over each array in loop 
        # at each iteration:
        # a) if not in hashset, append item to a hashset
        # b) if item is in hashset, we return True
        # c) if exhausted, then we'll return False
        # edge cases
        # can array be empty?

        hashset = set()
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
            else:
                return True
        return False





































        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # brute force
        # seen = [] # lookups using lists are O(n) time
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.append(i)
        # return False

        # nums.sort()
        # n = len(nums)

        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False # Time: O(nlogn), Space: O(1)

        # solution
        # hashset = set() # Hashsets have O(1) lookup time (unlike lists which are O(n))
        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        # return False # Time O(n), Space O(n)



        