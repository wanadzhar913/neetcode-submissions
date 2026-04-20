class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution #1
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i, 0)
        
        # sorted_map = sorted(map, key=lambda x: map[x], reverse=True)
        # return sorted_map[:k]

        # Solution #2
        from collections import Counter

        counts = Counter(nums).most_common(n=k)
        return [x[0] for x in counts]

        