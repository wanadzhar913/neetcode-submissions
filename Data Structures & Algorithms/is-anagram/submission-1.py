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
        # if len(s) != len(t):
        #     return False
        
        # seen = {}
        
        # for i in list(s):
        #     seen[i] = seen.get(i, 0) + 1
        
        # for j in list(t):
            
        #     seen[j] = seen.get(j, 0) + 1
        
        # if sum(seen.values()) == 0:
        #     return True
        # else:
        #     return False

        # Most Optimal - O(n)
        from collections import Counter

        return Counter(s) == Counter(t)
        