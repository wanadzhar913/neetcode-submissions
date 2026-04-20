class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # solution 1
        # return [x for x in set(nums2) if x in set(nums1)]
        
        # solution 2
        seen = set(nums1)

        result = []
        for n in nums2:
            if n in seen:
                result.append(n)
                seen.remove(n)
        return result
            



        