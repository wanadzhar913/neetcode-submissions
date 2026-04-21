class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution (Brute Force)
        # initialize a hashmap, `counts`.
        # iterate through nums
        # as we iterate, counts[i] = counts.get(i, 0) + 1
        # after we get `counts`, we decompose it, and sort according to the .values() key.
        # and then return the top k

        # Solution (Optimal)

        # initialize a hashmap, `counts_s`
        # we also initialize an array, freq. This will contain our buckets, [] which are of length, len(nums) plus one.
        # iterate through nums
        # as we iterate, counts[i] = counts.get(i, 0) + 1
        # iterate through `counts_s`. We'll add the keys, into their respective buckets, ordered by their values.
        # Naturally, the keys that appear most will be on the right, and the least will appear on the left.
        # Finally, we iterate through `freq` and append to the `output` list.
        # After each append we check if len(output) == k. If yes, we return.

        # Solution #1 Time: O(n + mlogn), Space: O(n)
        # map = {}
        # for i in nums:
        #     map[i] = 1 + map.get(i, 0)
        
        # sorted_map = sorted(map.keys(), key=lambda x: map[x], reverse=True)
        # return sorted_map[:k]

        # Solution #2 Time: O(n + mlogn), Space: O(n)
        # from collections import Counter

        # counts = Counter(nums).most_common(n=k)
        # return [x[0] for x in counts]

        # Solution #3 Time: O(n), Space: O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            print(n, c)
            freq[c].append(n) # item `n` occurs `c` times.

        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
