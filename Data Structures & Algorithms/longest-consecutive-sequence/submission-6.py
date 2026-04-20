class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution: Brute Force
        nums_sorted = sorted(set(nums))
        max_count = 0
        count = 0
        for i, num in enumerate(nums_sorted):
            if i == 0:
                count += 1
                max_count = max(max_count, count)
                prev_num = num
                continue
            if num - prev_num == 1:
                count += 1
                max_count = max(max_count, count)
                prev_num = num
            else:
                prev_num = num
                max_count = max(max_count, count)
                count = 1
                continue
        
        return max_count

        