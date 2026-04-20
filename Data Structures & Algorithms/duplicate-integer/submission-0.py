class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        tracker = []
        for i in nums:
            if i in tracker:
                return True
            else:
                tracker.append(i)
        return False
        