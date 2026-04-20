class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution: Brute Force
        # 1. initialize a hashmap (defaultdict(list)) - key: (first anagram), value: list[of all anagrams]
        # 2. for i in strs:
        #    sorted(i)
        # 3. check if sorted anagram in strs.
        #    if yes: append to list
        #    if no: hashmap[i].append(i)
        # 4. return hashmap.values()

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

        # 1. we initialize an `anagrams` hashmap (defaultdict(list))
        # the key (is a list of all letters, as well as their count e.g., aba/baa/aab -> [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # the value is a list of words for the given anagram
        # 2. Now, for every word in strs:
        # 3. We check every character in word:
        # 4. We the get their character count (as per 1.)
        # 5. Use the `anagrams` hashmap and append the word to the anagram it belongs to.

        from collections import defaultdict

        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a .... z

            for char in s:
                count[ord(char) - ord("a")] += 1
            # convert to Tuple because list can't be keys (and are mutable)
            # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())