class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return [x for x in set(nums2) if x in set(nums1)]
        else:
            return [x for x in set(nums1) if x in set(nums2)]