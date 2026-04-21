class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        elements_only = [item[0] for item in counts.most_common(k)]
        return elements_only































        # Solution #1 Time: O(n + mlogn), Space: O(n)
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i, 0)
        
        # sorted_map = sorted(map, key=lambda x: map[x], reverse=True)
        # return sorted_map[:k]

        # Solution #2 Time: O(n + mlogn), Space: O(n)
        # from collections import Counter

        # counts = Counter(nums).most_common(n=k)
        # return [x[0] for x in counts]

        # Solution #3 Time: O(n), Space: O(n)
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]
        # print(freq)

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     print(n, c)
        #     freq[c].append(n) # item `n` occurs `c` times.

        # print(freq)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
