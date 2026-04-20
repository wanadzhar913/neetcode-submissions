class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach #1
        # s = list(s)
        # t = list(t)

        # s.sort()
        # t.sort()

        # if s == t:
        #     return True
        # else:
        #     return False

        # Approach #2
        if len(s) != len(t):
            return False
        
        seen_s = {}
        seen_t = {}
        
        for i in list(s):
            seen_s[i] = seen_s.get(i, 0) + 1
        
        for j in list(t):
            seen_t[j] = seen_t.get(j, 0) + 1
        
        if seen_t == seen_s:
            return True
        else:
            return False

        # Most Optimal - O(n)
        # from collections import Counter

        # return Counter(s) == Counter(t)
        