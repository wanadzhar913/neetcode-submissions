class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach #1 Space: O(1) or O(n), Time: O(nlogn)
        # s = list(s)
        # t = list(t)

        # s.sort()
        # t.sort()

        # if s == t:
        #     return True
        # else:
        #     return False

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

        # Approach 3 - Time/Space - O(n)
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

        # Most Optimal Time/Space - O(n)
        # from collections import Counter

        # return Counter(s) == Counter(t)
        