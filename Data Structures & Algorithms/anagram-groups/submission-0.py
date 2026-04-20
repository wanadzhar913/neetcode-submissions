class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        # if sorted(i) is in anagrams:
        #     anagrams[sorted(i)].append
        # else:
        #     anagrams[sorted(i)] == [sorted(i)]

        # output = 

        for i in strs:
            key = "".join(sorted(i))
            if key in anagrams:
                anagrams[key].append(i)
            else:
                anagrams[key] = [i]

        return list(anagrams.values())