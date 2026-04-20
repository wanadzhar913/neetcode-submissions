class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 3 - Time/Space - O(n)

        # initialize 2 hashmaps, s and t 
        # can be done together
            # iterate through s, get all the keys and values
            # iterate through t, get all the keys abd values
        # next, compare keys and values of s in t
            # if all same, return True, else False
        # edge cases: diff length, then can immediately return False

        if len(s) != len(t):
            return False

        map_s, map_t = {}, {}
        
        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1

        for j in map_s.keys():
            if map_s[j] != map_t.get(j, 0):
                return False
        return True

        # Approach #1 Space: O(1) or O(n), Time: O(nlogn + mlogm)
        # return sorted(s) == sorted(t)

        # Approach #2 Time/Space - O(n)
        # if len(s) != len(t):
        #     return False
        
        # seen_s = {}
        # seen_t = {}
        
        # for i in list(s):
        #     seen_s[i] = seen_s.get(i, 0) + 1
        
        # for j in list(t):
        #     seen_t[j] = seen_t.get(j, 0) + 1
        
        # if seen_t == seen_s: # or iterate through the keys manually
        #     return True
        # else:
        #     return False

        # Most Optimal Time/Space - O(n)
        # from collections import Counter

        # return Counter(s) == Counter(t)
        