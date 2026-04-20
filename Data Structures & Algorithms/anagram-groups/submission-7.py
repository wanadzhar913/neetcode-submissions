class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For approaches #1 and #2, sorting each word is: O(k log k)
        # So time complexity: O(n * k log k)
        # Solution #1: 
        # anagrams = {}

        # for i in strs:
        #     key = "".join(sorted(i))
        #     if key in anagrams:
        #         anagrams[key].append(i)
        #     else:
        #         anagrams[key] = [i]

        # return list(anagrams.values())

        # Solution #2 (Cleaner)
        # from collections import defaultdict

        # anagrams = defaultdict(list)

        # for s in strs:
        #     key = "".join(sorted(s))
        #     anagrams[key].append(s)

        # return list(anagrams.values())

        # Solution #3 (Optimal)
        from collections import defaultdict

        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a .... z

            for c in s:
                count[ord(c) - ord("a")] += 1
            # convert to Tuple because list can't be keys (and are mutable)
            # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())