class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution: Brute Force
        # 1. Use hashset to remove duplicates
        # 2. Sort them in ascending order. We do this because:
        # 3. At each step, it allows us to see if the diff is 1.
        # 4. If yes, we can update a `counter. It'd also help if we've a `max_counter`
        # variable to keep track of the global maximum.
        # nums_sorted = sorted(set(nums))
        # max_count = 0
        # count = 0
        # for i, num in enumerate(nums_sorted):
        #     if i == 0:
        #         count += 1
        #         max_count = max(max_count, count)
        #         prev_num = num
        #         continue
        #     if num - prev_num == 1:
        #         count += 1
        #         max_count = max(max_count, count)
        #         prev_num = num
        #     else:
        #         prev_num = num
        #         max_count = max(max_count, count)
        #         count = 1
        #         continue
        
        # return max_count

        # Solution: Clean Brute Force
        # Remove duplicates + sort
        # Time: O(n+mlogm+m) -> set(nums) is O(n) time, sorted() is O(mlogm), for loop is m
        # Space: O(n) -> set(nums) is O(m) time, but in the worst case is O(n)
        # nums_sorted = sorted(set(nums))
        
        # if not nums_sorted:
        #     return 0
        
        # max_count = 1
        # count = 1
        # prev_num = nums_sorted[0]
        
        # for num in nums_sorted[1:]:
        #     if num - prev_num == 1:
        #         count += 1
        #     else:
        #         count = 1
            
        #     max_count = max(max_count, count)
        #     prev_num = num
        
        # return max_count

        # Solution #3 Time/Space: O(n)
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
        