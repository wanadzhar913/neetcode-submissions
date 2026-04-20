class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i, 0)
        
        sorted_map = sorted(map, key=lambda x: map[x], reverse=True)
        return sorted_map[:k]
        